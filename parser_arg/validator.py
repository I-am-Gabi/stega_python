import os.path
from image_processing.exceptions.FileInputError import FileInputError


def validator_file(file):
    try:
        return os.path.isfile(file)
    except FileInputError as e:
        "I/O error({0}): {1}".format(e.errno, e.strerror)