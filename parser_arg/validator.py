import os.path
import magic


def validator_file(file):
    try:
        return os.path.isfile(file)
    except TypeError as e:
        "I/O error({0})".format(e)


def validator_pattern(pattern):
    try:
        return pattern in ("direct", "reverse")
    except TypeError as e:
        "Pattern error({0})".format(e)


def validator_channels(channels):
    if len(channels) > 4:
        return False
    if "gray" in channels and len(channels) != 1:
        return False
    if len(set(channels)) != len(channels):
        return False
    if not list(set(channels).intersection(['red', 'green', 'blue'])):
        return False
    return True


def validator_signature_file(file_name):
    signature_valides = ["png", "bmp"]

    try:
        file_signature = magic.from_file(file_name).lower().split(' ')
        if list(set(signature_valides).intersection(file_signature)):
            return True
        return False
    except Exception as e:
        "File signature error({0})".format(e)
