from parser_arg.parser import parser
from stegano.revelation.stegano import reveal


def main():
    arg = parser()

    if "revelation" in arg:
        msg = reveal(arg)
    else:
        msg = dissimulation(arg)

    if msg:
        print "steganography finish"

    file_output = open(arg[1], 'r+b')
    file_output.write(str(msg))

if __name__ == "__main__":
    main()
