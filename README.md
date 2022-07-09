# LRP

Implementation of Layer-wise Relevance Propagation (LRP) algorithm together with quantitative evaluation metrics to compare heatmap explanations objectively.

## Features

Explainability:

- Layer-wise Relevance Propagation (LRP)

Quantitative Evaluation:

- Pixel Flipping (PF), also known as Region Perturbation (RP)
  - Perturbation modes:
    - inpainting
    - random
  - Sort objectives:
    - most relevant first (MoRF), also known as activation curve
    - least relevant first (LRF), also known as pruning curve
    - random
- AUC (Area Under the Curve), also known as AUAC (Area Under the Activation Curve) or AU-MSE (Area Under the Mean Squared Error Curve) depending on the sort objective

### Showcase

**LRP** ([lrp-tutorial](https://git.tu-berlin.de/gmontavon/lrp-tutorial) composite) and **PF** with **inpainting** perturbation mode and sort objective **MoRF**.

<p align="center" width="100%">
    <img width="50%" src="./docs/images/castle-lrp-pf-auc-inpainting.png">
</p>

Classification scores of castle image with **inpainting** perturbation mode

<p align="center" width="100%">
    <img width="50%" src="./docs/images/castle-pf-auc-inpainting.png">
</p>

---

<details>
<summary>PF perturbation mode random</summary>
<p>

**LRP** ([lrp-tutorial](https://git.tu-berlin.de/gmontavon/lrp-tutorial) composite) and **PF** with **random** perturbation mode and sort objective **MoRF**.

<p align="center" width="100%">
    <img width="50%" src="./docs/images/castle-lrp-pf-auc-random.png">
</p>

Classification scores of castle image with random perturbation mode

<p align="center" width="100%">
    <img width="50%" src="./docs/images/castle-pf-auc-random.png">
</p>

</p>
</details>

## Requirements

- `python3` >= 3.9

## Installation

## Usage

Refer to [demo.ipynb](./demo.ipynb) for an example of Layer-wise Relevance Propagation (LRP), Pixel-Flipping (PF) and Area under the Curve (AUC).

## Related Projects

- Sequential LRP implementation: [gmontavon/lrp-tutorial](https://git.tu-berlin.de/gmontavon/lrp-tutorial)
  > Tutorial on how to implement LRP
- Updated version of `gmontavon/lrp-tutorial`: [rodrigobdz/lrp-tutorial](https://git.tu-berlin.de/rodrigobdz/lrp-tutorial)
- Forward-hook LRP implementation: [chr5tphr/zennit](https://github.com/chr5tphr/zennit)
  > Implementation of LRP-based methods in PyTorch
- [`innvestigate`](https://github.com/albermax/innvestigate)-based LRP implementation: [moboehle/Pytorch-LRP](https://github.com/moboehle/Pytorch-LRP)

## Citation

## Credits

- The structure of this readme is based on [minimal-readme](https://github.com/rodrigobdz/minimal-readme)

This implementation is based on insights from:

- LRP overview paper

  > G. Montavon, A. Binder, S. Lapuschkin, W. Samek, K.-R. Müller
  > [Layer-wise Relevance Propagation: An Overview](https://doi.org/10.1007/978-3-030-28954-6_10)
  > in Explainable AI: Interpreting, Explaining and Visualizing Deep Learning, Springer LNCS, vol. 11700, 2019

- Original LRP paper

  > S. Bach, A. Binder, G. Montavon, F. Klauschen, K.-R. Müller, W. Samek
  > [On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation](https://doi.org/10.1371/journal.pone.0130140)
  > PloS ONE 10 (7), e0130140, 2015

- [ECML/PKDD 2020 Tutorial: Explainable AI for Deep Networks: Basics and Extensions (Part 3)](http://heatmapping.org/slides/2020_ECML_3.pdf)

## License

[MIT](LICENSE) © [rodrigobdz](https://github.com/rodrigobdz/)