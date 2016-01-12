import os.path


def validator_file(file):
    try:
        return os.path.isfile(file)
    except TypeError as e:
        "I/O error({0})".format(e)