"""
red = 2
green = 1
blue = 0
"""
from util.binary import get_bit, set_bit
import re


def uncover(image, pattern, bits, channel):
    h, w, c = image.shape
    byte = 0
    msg = ""
    index_byte = 7
    magic = "HELP"

    if pattern:
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
            pixel = image[i, j, channel]

            for bit in range(bits - 1, -1, -1):
                byte = set_bit(byte, index_byte, get_bit(pixel, bit))
                index_byte -= 1
                if magic in msg:
                    msg = re.sub(magic, '', msg)
                    return msg
                elif index_byte == -1:
                    msg += chr(byte)
                    byte = 0
                    index_byte = 7

    return msg
    # return (byte, index_byte)
