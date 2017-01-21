# -*- coding: utf-8 -*-
# Elizabeth Sh., Jan 2017
# https://github.com/ms-lilibeth
import numpy
import random


def generator(noise_probability):
    if not isinstance(noise_probability, float) or noise_probability < 0 or noise_probability > 1:
        raise ValueError("generator: noise_probability parameter must be float in range [0, 1]")
    pass


#  Implements Xiaolin Wu's line algorithm
def _draw_line(coord1, coord2):
    pass


def _save_in_pgm(img):
    with open("image.pgm", 'w') as f:
        f.write("P2\n")
        f.write("500 500\n")
        # the image itself
