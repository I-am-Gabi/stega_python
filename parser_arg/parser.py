import getopt
from validator import *
import sys


def parser():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:p:o:b:c:h", ["help", "output", "input", "operation"])
    except getopt.GetoptError as err:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    operation = ""
    input_filename = ""
    output_filename = ""
    pattern = "direct"
    bits = 1
    channels = []

    for opt, arg in opts:
        if opt in ("-i", "--input"):
            input_filename = arg
        elif opt == "-p":
            pattern = arg
        elif opt in ("-o", "--output"):
            output_filename = arg
        elif opt == "-b":
            bits = int(arg)
        elif opt == "-c":
            channels = arg.lower().split(',')
            if len(channels) > 1:
                print 'choice just one channel'
                sys.exit(2)
        elif opt == "-operation":
            operation = arg
        elif opt in ("-h", "--help"):
            print("python stegano.py -i resources/images/direct_Green_1.png -o resources/txt/output.txt -b 1 -c green")
            sys.exit()
        else:
            print "unhandled option"
            sys.exit(2)

    if not (validator_file(input_filename) and validator_file(output_filename) and validator_pattern(
            pattern) and validator_channels(channels) and validator_file_signature(input_filename)) \
            or not validator_bit_factor(bits):
        print "Error Argument"
        sys.exit(2)

    if "red" in channels:
        channels = 2
    elif "green" in channels:
        channels = 1
    else:
        channels = 0

    return input_filename, output_filename, pattern, bits, channels, operation


if __name__ == "__main__":
    parser()
