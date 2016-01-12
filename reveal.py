from parser_arg.parser import parser
from stegano.stegano import reveal


def main():
    arg = parser()

    msg = reveal(arg)
    string = ""

    file = open(arg[1],'ab')

    for c in msg:
        if c != 255:
            string += chr(c)
    file.write(str(string))
    #print msg[0]
    #print chr(msg[0])
    #file.write(str(unichr(c) for c in msg))
    #file.write((''.join(chr(i) for i in msg)).encode('ascii'))
    #fileByteArray = bytearray(msg)
    #file.write(str(msg))

if __name__ == "__main__":
    main()