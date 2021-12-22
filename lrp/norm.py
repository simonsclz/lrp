r'''Normalization functions and pre-processing of input data
'''


from typing import Callable, List
import torch
import numpy


class StandardScoreNorm:
    r'''Normalize matrix by calculating standard score, i.e., subtracting mean and dividing by standard deviation of the dataset.

    Source: https://github.com/chr5tphr/zennit/blob/cc9ac0f3016e1b842f2c60e8986c794b2ae7096e/share/example/feed_forward.py#L32-L38
    '''

    def __init__(self, mean: List[float], std: List[float]) -> Callable[[torch.Tensor], torch.Tensor]:
        r'''Convert mean and standard deviation to tensors

        :param mean: Mean of the dataset
        :param std: Standard deviation of the dataset
        '''
        self.mean = torch.tensor(mean)[None, :, None, None]
        self.std = torch.tensor(std)[None, :, None, None]

    def __call__(self, matrix: torch.Tensor) -> torch.Tensor:
        r'''Calculate standard score

        :param matrix: Matrix to be normalized
        :returns: Normalized matrix
        '''
        return (matrix - self.mean) / self.std


class ILSVRC2012_BatchNorm(StandardScoreNorm):
    r'''Normalize batch of images from ILSVRC2012 dataset

    Mean and std are calculated from the dataset ImageNet
    https://github.com/Cadene/pretrained-models.pytorch/blob/8aae3d8f1135b6b13fed79c1d431e3449fdbf6e0/pretrainedmodels/models/torchvision_models.py#L64-L65
    '''

    def __init__(self) -> Callable[[torch.Tensor], torch.Tensor]:
        super().__init__(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])


def normalize_rgb_img(img: numpy.array, max_value: float = 255.0) -> numpy.array:
    r'''Normalize RGB image

    Divide by 255 (max. RGB value) to normalize pixel values to [0,1]

    :param img: RGB image
    :param max_value: Maximum value of the RGB image

    :returns: Normalized RGB image
    '''
    return img / max_value
