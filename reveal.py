from parser_arg.parser import parser
from stegano.stegano import reveal
import difflib


def main():
    arg = parser()

    msg = reveal(arg)
    if msg:
        print "steganography finish"

    file_output = open(arg[1], 'r+b')
    file_output.write(str(msg))

if __name__ == "__main__":
    main()
