# DINOv2 Feature Extraction

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Development](#development)
- [License](#license)

## 🔍 Overview

This project implements a feature extraction pipeline using the DINOv2 (Vision Transformer) model. It processes images, extracts visual features, and performs some basic analysis on the extracted features.

## ✨ Features

- Download and process images from URLs
- Resize images to a specified size
- Extract visual features using the DINOv2 model
- Compute average features and perform L2 normalization
- Calculate the sum of elements and L2 norm for each processed feature

## 📦 Requirements

- Python 3.10 or higher
- Poetry for dependency management
- CUDA-capable GPU (optional, for faster processing)

## 🚀 Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/dinov2-feature-extraction.git
   cd dinov2-feature-extraction
   ```

2. Install Poetry:
   Follow the installation instructions in the [official Poetry documentation](https://python-poetry.org/docs/#installation).

3. Install the project dependencies:
   ```
   poetry install
   ```

## 🖥️ Usage

1. Activate the Poetry environment:
   ```
   poetry shell
   ```

2. Run the feature extraction script:
   ```
   make run
   ```

   Or alternatively:
   ```
   python3 feature_extraction.py
   ```

3. The script will process the images specified in `image_urls.json` and output the results.

## 📁 Project Structure

- `feature_extraction.py`: Main script for feature extraction
- `image_urls.json`: Configuration file containing image URLs to process
- `Makefile`: Contains commands for running the script and development tools
- `pyproject.toml`: Poetry configuration file
- `poetry.lock`: Lock file for Poetry dependencies

## 🛠️ How It Works

1. The script reads image URLs from `image_urls.json`.
2. It downloads and loads each image.
3. Images are resized to 100x100 pixels.
4. The DINOv2 model processes each image to extract features.
5. Features are averaged over spatial dimensions and normalized.
6. The script outputs the shape, sum of elements, and L2 norm for each processed feature.

## 👨‍💻 Development

This project uses several development tools to maintain code quality:

- **Black**: Code formatter
- **isort**: Import sorter
- **flake8**: Linter
- **mypy**: Static type checker
- **pylint**: Code analysis tool

To run all checks:

```
make check
```

To run individual tools:

```
make black
make isort
make flake8
make mypy
make pylint
```

To clean up Python cache files:

```
make clean
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information or to report issues, please open an issue on the GitHub repository.
