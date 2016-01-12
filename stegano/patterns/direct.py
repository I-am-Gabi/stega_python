"""
channel standard is
red = 2
green = 1 <--
blue = 0

pixel = set_bit(pixel, 1, get_bit(pixel, 1))
image.itemset((i, j, 2), pixel)
"""
from util.binary import get_bit, set_bit

def uncover(image):
    h, l, c = image.shape
    byte = 0
    msg = []
    index_byte = 0

    for i in range(0, h):
        for j in range(0, l):
            pixel = image[i, j, 1]
            byte = set_bit(byte, index_byte, get_bit(pixel, 0))
            index_byte += 1

            if "HELP" in str(byte):
                return byte
            elif index_byte == 8:
                msg.append(byte)
                byte = index_byte = 0
    #print msg
    return msg
