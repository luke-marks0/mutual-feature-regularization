# Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders

This repository contains code and experiments for the paper "Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders". We use mutual learning to train sparse autoencoders (SAEs) to achieve lower reconstruction loss, and give evidence that they also learn more information about the input features.

## Table of Contentshttps://github.com/luke-marks0

- [Installation](#installation)
- [Experiments](#experiments)
  - [Training SAEs on Synthetic Data](#training-saes-on-synthetic-data)
  - [Training SAEs on GPT-2 Small MLP Activations](#training-saes-on-gpt-2-small-mlp-activations)
  - [Training SAEs to Denoise EEG Data](#training-saes-to-denoise-eeg-data)
- [Configuration](#configuration)
- [Citation](#citation)
- [License](#license)

## Installation

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/luke-marks0/mutual-feature-regularization.git
   cd repository
2. Install required dependencies:
```
pip install -r requirements.txt
```

3. For the EEG experiment, ensure you have the necessary permissions to download and access the datasets.

### Experiments

1. Training SAEs on Synthetic Data
This experiment involves training SAEs on synthetic data that has known ground truth features. These features are designed to mimic superposed features in neural networks, allowing for easy evaluation of how well the SAEs learn these features.

To run this experiment, use the following command:

```
python main.py --config configs/synthetic.yaml
````

2. Training SAEs on GPT-2 Small MLP Activations
This experiment uses activations from the MLP layers (by default, layer 0) of GPT-2 Small.

Run the experiment with:
```
python main.py --config configs/gpt2.yaml
```
3. Training SAEs to Denoise EEG Data
In this experiment, SAEs are trained to denoise EEG data from the TUH EEG corpus. Running it requires credentials to access the TUH EEG corpus, which should be set as the environment variables `EEG_USERNAME` and `EEG_PASSWORD`.

To run the EEG denoising experiment, use:

```
python main.py --config configs/eeg.yaml
```

# Citation


If you use this code or refer to the paper, please cite it as follows:
```bibtex
@misc{marks2024eSAEinterpretability,
      title={Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders}, 
      author={Luke Marks and Alisdair Paren and David Krueger and Fazl Barez},
      year={2024},
      eprint={2411.01220},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2411.01220}, 
}
```



