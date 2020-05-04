'''
Author: Elijah Sawyers
Email: elijahsawyers@gmail.com
Date: 03/07/19
Overview: This file contains the functionality for converting a pdf to png.
'''

import sys
from wand.image import Image

if __name__ == "__main__":
    pdf = Image(filename=sys.argv[1])

    with pdf as pdf_to_convert:
        with pdf_to_convert.convert('png') as png:
            png.save(filename=sys.argv[2])
