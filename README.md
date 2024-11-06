# Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders

This repository contains code and experiments for enhancing the interpretability of neural networks using Feature-Aligned Sparse Autoencoders (SAEs). The approach presented in this work helps uncover latent features and improve the interpretability of complex models by aligning sparse features with known ground truth or activations.

## Table of Contentshttps://github.com/luke-marks0

- [Overview](#overview)
- [Installation](#installation)
- [Experiments](#experiments)
  - [Training SAEs on Synthetic Data](#training-saes-on-synthetic-data)
  - [Training SAEs on GPT-2 Small MLP Activations](#training-saes-on-gpt-2-small-mlp-activations)
  - [Training SAEs to Denoise EEG Data](#training-saes-to-denoise-eeg-data)
- [Configuration](#configuration)
- [Citation](#citation)
- [License](#license)

## Overview

In this work, we explore different experiments to evaluate the effectiveness of Sparse Autoencoders (SAEs) for interpreting neural network activations and features. Our goal is to align the sparse features learned by the SAE with known ground truths, such as synthetic features, model activations, or real-world data like EEG recordings.

### Key Features:
- **Interpretability**: Improve model transparency by learning sparse features aligned with known activations or ground truth.
- **Flexibility**: Implemented experiments on synthetic data, transformer model activations (GPT-2), and EEG data for diverse applications.
- **Data Handling**: The repository includes code to automatically handle data preprocessing, such as downloading and formatting EEG data.

## Installation

### Prerequisites
- Python 3.7+
- Recommended: Use a virtual environment (e.g., `venv` or `conda`) to manage dependencies.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/luke-marks0/mutual-feature-regularization.git
   cd repository
2. Install required dependencies:
```
pip install -r requirements.txt
```

3. For data-related experiments (e.g., EEG), ensure you have the necessary permissions to download and access the datasets. See the Data section for more details.


### Experiments

1. Training SAEs on Synthetic Data
This experiment involves training SAEs on synthetic data that has known ground truth features. These features are designed to mimic feature superposition in neural networks, allowing for easy evaluation of how well the SAE approximates these features.

To run this experiment, use the following command:

```
python main.py --config configs/synthetic.yaml
````

2. Training SAEs on GPT-2 Small MLP Activations
This experiment uses activations from the MLP layers (by default, layer 0) of GPT-2 Small. Training SAEs on these activations allows us to assess how well the SAE can interpret neural activations in a transformer model.

Run the experiment with:
```
python main.py --config configs/gpt2.yaml
```
3. Training SAEs to Denoise EEG Data
In this experiment, SAEs are trained to denoise EEG data from the TUH EEG corpus. The code handles downloading and formatting the data, making it straightforward to train the SAE for real-world data denoising.

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



