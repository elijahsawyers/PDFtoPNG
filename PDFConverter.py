'''
    Author: Elijah Sawyers
    Date: 03/07/19
    Overview: This file contains the functionality for converting a pdf to png.
'''

import sys
from wand.image import Image

'''This class can convert pdf files into png files.'''
class PDFConverter: 

    # Initialize the PDF converter.
    def __init__(self, pdfFilePath):
        self.pdfFile = Image(filename=pdfFilePath)

    # Converts a pdf file into a png file.
    def convertToPng(self, newFilePath):
        with self.pdfFile as pdfToConvert:
            # Convert to png.
            with pdfToConvert.convert("png") as convertedPdf:
                convertedPdf.save(filename=newFilePath)

# Run the script.
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Usage: python PDFConverter.py PDFPath PNGName")
    else:
        pdfConverter = PDFConverter(sys.argv[1])
        pdfConverter.convertToPng(sys.argv[2])
