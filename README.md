# PDF to PNG
> A simple Python script to convert a PDF to a PNG.

## Prerequisites

Ensure that you have ImageMagick and Ghostscript installed. If not, follow the installation steps on their websites.

## Setup

Create a virtual environment and install the project requirements.

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Running the script

To run the script, pass in the PDF file path and name as the first command-line argument, and pass in the file path and name of where to save the converted PNG as the second command-line argument. 

```
python converter.py ~/path/to/convert/PDFFileName.pdf ~/path/to/save/PNGFileName.png
```

## Build With

* [GhostScript](https://www.ghostscript.com/)
* [ImageMagic](https://www.imagemagick.org/)
* [Wand](http://docs.wand-py.org/en/0.4.1/index.html)

## Authors

* [Elijah Sawyers](https://github.com/elijahsawyers)
