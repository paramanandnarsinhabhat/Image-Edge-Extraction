
# Image Edge Extraction

This repository contains the code for extracting edges from images using various filters provided by the `scikit-image` library in Python. Edge detection is a common operation in image processing that helps in understanding the features within an image.

## Structure

- `gooddad`: Virtual environment directory.
- `images`: Directory containing the image files.
- `notebook`: Jupyter notebooks for interactive development and testing.
- `source`: Source code for edge extraction.

## Installation

Before running the scripts, ensure you have the required libraries installed. Activate your virtual environment and install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

The script `edge_extraction.py` in the `source` directory demonstrates how to use the Sobel and Prewitt kernels to extract horizontal and vertical edges from an image. It reads an image in grayscale, applies edge detection filters, and displays the results.

To run the script, navigate to the `source` directory and execute:

```bash
python edge_extraction.py
```

## Edge Detection Process

The script performs the following operations:

1. It loads an image in grayscale.
2. It calculates horizontal and vertical edges using Sobel and Prewitt kernels.
3. It displays the original image and the edge-detected images.

## Requirements

- `scikit-image`: For image reading and edge detection filters.
- `matplotlib`: For displaying images.

Make sure to adjust the path to the image in the `imread` function according to your local setup.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the terms of the MIT license

