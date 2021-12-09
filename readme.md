# LRP

Implementation of Layer-wise Relevance Propagation (LRP) algorithm.

## Requirements

- `python3`

## Installation

1. Install python dependencies.

   ```sh
   # Create python virtual environment (venv) called lrp-env
   python3 -m venv lrp-env

   # Activate venv
   source lrp-env/bin/activate

   # Install dependencies defined in requirements.txt
   python3 -m pip install --requirement requirements.txt
   ```

## Usage

Refer to [lrp.ipynb](./lrp.ipynb) for an example.

## Related Projects

- (Sequential) [gmontavon/lrp-tutorial](https://git.tu-berlin.de/gmontavon/lrp-tutorial) - Tutorial on how to implement LRP
- (Forward-hook) [chr5tphr/zennit](https://github.com/chr5tphr/zennit) - Implementation of LRP-based methods in PyTorch

## Credits

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

[MIT](LICENSE) © [rodrigobdz](https://rodrigobdz.github.io/).