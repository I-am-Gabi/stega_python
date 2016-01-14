import getopt
from validator import validator_file, validator_pattern, validator_channels, validator_signature_file
import sys


def parser():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:p:o:b:c:h", ["help", "output", "input"])
    except getopt.GetoptError as err:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

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
        elif opt in ("-h", "--help"):
            print("in progress")
            sys.exit()
        elif opt in ("-o", "--output"):
            output_filename = arg
        elif opt == "-b":
            bits = int(arg)
        elif opt == "-c":
            channels = arg.lower().split(',')
            if len(channels) > 1:
                print 'choice just one channel'
                sys.exit(2)
        else:
            print "unhandled option"
            sys.exit(2)

    if not validator_file(input_filename) \
            or not validator_file(output_filename) \
            or not validator_pattern(pattern) \
            or not validator_channels(channels) \
            or not validator_signature_file(input_filename):
        print "Error Argument"
        sys.exit(2)

    if "red" in channels:
        channels = 2
    elif "green" in channels:
        channels = 1
    else:
        channels = 0

    return (input_filename, output_filename, pattern, bits, channels)


if __name__ == "__main__":
    parser()
