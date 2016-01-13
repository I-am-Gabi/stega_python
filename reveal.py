from parser_arg.parser import parser
from stegano.stegano import reveal
import filecmp


def main():
    arg = parser()

    msg = reveal(arg)
    file_output = open(arg[1], 'wb')
    file_output.write(str(msg))

    print filecmp.cmp("resources/txt/originaltext1.txt", arg[1], shallow=False)

if __name__ == "__main__":
    main()
