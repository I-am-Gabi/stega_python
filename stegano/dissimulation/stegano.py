from image.image import read_image
from stegano.revelation.patterns.sequential import uncover


def reveal(args):
    response = ""
    if "direct" in args:
        response = uncover(read_image(args[0]), True, args[3], args[4])
    elif "reverse" in args:
        response = uncover(read_image(args[0]), False, args[3], args[4])

    if type(response) == str:
        return response
