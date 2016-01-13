"""
channel standard is
red = 2
green = 1 <--
blue = 0

pixel = set_bit(pixel, 1, get_bit(pixel, 1))
image.itemset((i, j, 2), pixel)
"""
from util.binary import get_bit, set_bit
import re, sys


def uncover(image, pattern):
    h, w, c = image.shape
    byte = 0
    msg = ""
    index_byte = 7
    magic = "HELP"

    if (pattern):
        start_line = 0
        stop_line = h
        start_column = 0
        stop_column = w
        tax = 1
    else:
        start_line = h - 1
        stop_line = -1
        start_column = w - 1
        stop_column = -1
        tax = -1

    for i in range(start_line, stop_line, tax):
        for j in range(start_column, stop_column, tax):
            pixel = image[i, j, 2]
            byte = set_bit(byte, index_byte, get_bit(pixel, 0))
            index_byte -= 1

            if magic in msg:
                msg = re.sub(magic, '', msg)
                return msg
            elif index_byte == -1:
                msg += chr(byte)
                byte = 0
                index_byte = 7

    print "there is not magic number in the file"
    sys.exit(2)
