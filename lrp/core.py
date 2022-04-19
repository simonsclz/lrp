r'''Composite Layer-wise Relevance Propagation using rules defined by layer
'''


__author__ = 'Rodrigo Bermudez Schettino (TU Berlin)'
__credits__ = ['Rodrigo Bermudez Schettino (TU Berlin)']
__maintainer__ = 'Rodrigo Bermudez Schettino (TU Berlin)'
__email__ = 'r.bermudezschettino@campus.tu-berlin.de'
__status__ = 'Development'


from typing import Union, Dict, List, Tuple, Optional
import torch
import copy
import pf.utils
from . import rules, builtin, plot


class LRP:
    r'''Compute relevance propagation using Layer-wise Relevance Propagation algorithm'''

    def __init__(self, model: torch.nn.Module) -> None:
        r'''Prepare model for LRP computation

        :param model: Model to be explained
        '''
        self.model = copy.deepcopy(model)
        self.model.eval()
        self.name_map: List[Tuple[List[str], rules.LrpRule,
                                  Dict[str, Union[torch.Tensor, float]]]] = []
        self.relevance_scores_nchw: Optional[torch.Tensor] = None

    def convert_layers(self, name_map:
                       List[
                           Tuple[
                               # Layer names
                               List[str],

                               # LRP rule to apply
                               rules.LrpRule,

                               # Parameters for rule
                               Dict[str, Union[torch.Tensor, float]]
                           ]
                       ]) -> None:
        r'''Add LRP support to layers according to given mapping

        :param name_map: List of tuples containing layer names, LRP rule and parameters
        '''

        self.name_map = name_map

        for name, layer in self.model.named_modules():
            # Check which rule to apply
            rule = self.mapping(name)

            # No rule to apply
            if rule is None:
                continue

            # Unwrap tuple containing rule and its parameters
            rule_class, rule_kwargs = rule

            # Initialize rule class
            lrp_layer = rule_class(layer, **rule_kwargs)

            # Apply rule to named layer
            builtin.rsetattr(self.model, name, lrp_layer)

    def mapping(self, name: str) -> Optional[Tuple[rules.LrpRule, Dict[str, Union[torch.Tensor, float]]]]:
        r'''Get LRP rule and parameters for layer with given name

        :param name: Layer name
        :return: LRP rule and parameters or None if no rule is found
        '''
        for layer_names, rule, rule_kwargs in self.name_map:
            # Apply rule only to layers included in mapping
            if name in layer_names:
                return rule, rule_kwargs

        return None

    def relevance(self, input_nchw: torch.Tensor) -> torch.Tensor:
        r'''Compute relevance for input_nchw by applying Gradient*Input

        Source: "Algorithm 8 LRP implementation based on forward hooks" in
        "Toward Interpretable Machine Learning: Transparent Deep Neural Networks and Beyond"

        :param input_nchw: Input to be explained
        :returns: Relevance for input_nchw
        '''

        pf.utils._ensure_nchw_format(input_nchw)

        # Prepare to compute input gradient
        # Reset gradient
        self.model.zero_grad()
        input_nchw.requires_grad = True

        # Set default values for relevance, in case ZBoxrule is not used
        low = high = c2 = c3 = 0

        # Vars to retrieve gradients from first layer
        first_layer: torch.nn.Module = self.model.features[0]

        if isinstance(first_layer, rules.LrpZBoxRule):
            # Access high and low copy layers in first layer.
            low: torch.Tensor = first_layer.low
            high: torch.Tensor = first_layer.high

            # Reset stored gradients.
            low.grad = None
            high.grad = None

        # Reset stored gradients
        input_nchw.grad = None

        # Compute explanation by storing value of gradient in input_nchw.grad.
        # Only the predicted class is propagated backwards.
        #
        # 1. Compute forward pass
        forward_pass: torch.Tensor = self.model(input_nchw)

        # 2. Get index maximum activation in the output layer (index of the predicted class)
        idx: torch.Tensor = forward_pass.max(dim=1).indices

        # 3. Create new tensor where elements are tuples (i, idx[i]) with i: counter.
        # Tensor looks like this: [0, 1, ..., len(idx)]
        i: torch.Tensor = torch.arange(len(idx))
        stacked_idx: torch.Tensor = torch.stack((i, idx), dim=1)

        # 4. One-hot encoding for the predicted class in each sample.
        # This is a mask where the predicted class is True and the rest is False.
        batch_size: int = input_nchw.shape[0]
        number_of_classes: int = forward_pass.shape[1]
        # Init zeros tensor for one-hot encoding
        gradient: torch.Tensor = torch.zeros(batch_size,
                                             number_of_classes,
                                             dtype=torch.bool)
        # Set the predicted class to True
        gradient[stacked_idx[:, 0], stacked_idx[:, 1]] = True

        # 5. Compute gradient of output layer for the predicted class of each sample.
        forward_pass.backward(gradient=gradient)

        if isinstance(first_layer, rules.LrpZBoxRule):
            # Compute gradients
            c2, c3 = low.grad, high.grad

        # Compute input gradient
        c1 = input_nchw.grad

        # Compute relevance
        self.relevance_scores_nchw = input_nchw * c1 + low * c2 + high * c3
        return self.relevance_scores_nchw.detach()

    @staticmethod
    def heatmap(relevance_scores_nchw: torch.Tensor, width: int = 4, height: int = 4) -> None:
        r'''Create heatmap of relevance

        :param relevance_scores_nchw: Relevance tensor with N3HW format
        :param width: Width of heatmap
        :param height: Height of heatmap
        '''
        pf.utils._ensure_nchw_format(relevance_scores_nchw)
        # Convert each heatmap from 3-channel to 1-channel.
        # Channel dimension is now omitted.
        r_nhw = relevance_scores_nchw.sum(dim=1)

        # Loop over relevance scores for each image in batch
        for r_hw in r_nhw:
            plot.heatmap(r_hw.detach().numpy(), width, height)
