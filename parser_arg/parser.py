import getopt
from validator import validator_file, validator_pattern
import sys


def parser():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:p:ho:", ["help", "output", "input"])
    except getopt.GetoptError as err:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    input_filename = ""
    output_filename = ""
    pattern = ""

    for opt, arg in opts:
        if opt in ("-i", "--input"):
            input_filename = arg
        elif opt == "-p":
            pattern = arg
        elif opt in ("-h", "--help"):
            print("in progress")
            sys.exit()
        elif opt in ("-o", "--output"):
            output_filename = arg
        else:
            print "unhandled option"
            sys.exit(2)

    if not validator_file(input_filename) or not validator_file(output_filename) or not validator_pattern(pattern):
        sys.exit(2)

    return (input_filename, output_filename, pattern)


if __name__ == "__main__":
    parser()
