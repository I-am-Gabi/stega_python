import os.path


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
    # TODO: see this
    """if set(channels).issubset(set(['red', 'green', 'blue'])):
        print channels in ['red', 'green', 'blue']
        return False"""
    return True

