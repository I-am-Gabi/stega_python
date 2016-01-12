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
