import os.path
import magic


def validator_file(name_file):
    try:
        return os.path.isfile(name_file)
    except TypeError as e:
        "I/O error({0})".format(e)
        return False


def validator_pattern(pattern):
    try:
        return pattern in ("direct", "reverse")
    except TypeError as e:
        "Pattern error({0})".format(e)
        return False


def validator_channels(channels):
    try:
        if len(channels) > 4 or len(channels) == 0:
            return False
        if "gray" in channels and len(channels) != 1:
            return False
        if len(set(channels)) != len(channels):
            return False
        if channels != list(set(channels).intersection(["red", "green", "blue"])):
            return False
        return True
    except TypeError as e:
        "Channels error({0})".format(e)
        return False


def validator_file_signature(file_name):
    try:
        signature_valid = ["png", "bmp", "pgm", "ppm"]

        file_signature = magic.from_file(file_name).lower().split(' ')
        if list(set(signature_valid).intersection(file_signature)):
            return True
        return False
    except Exception as e:
        "File signature error({0})".format(e)
        return False


def validator_bit_factor(bit):
    try:
        if bit > 8 or bit <= 0:
            return False
        return True
    except Exception as e:
        "Bit Factor error({0})".format(e)
        return False
