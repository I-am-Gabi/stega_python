from image.image import read_image
from patterns.sequential import uncover


def reveal(args):
    if "direct" in args:
        return uncover(read_image(args[0]), True)
    elif "reverse" in args:
        return uncover(read_image(args[0]), False)
