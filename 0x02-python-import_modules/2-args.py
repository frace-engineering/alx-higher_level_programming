#!/usr/bin/python3
def main():
    pass

if __name__=="__main__":
    import sys
    nargs = len(sys.argv) - 1
    if (nargs == 0):
        print("{:d} argument.".format(nargs))
    elif (nargs == 1):
        print("{:d} argument:".format(nargs))
    else:
        print("{:d} arguments:".format(nargs))
        for i in range(len(sys.argv)):
            if (i <= 1):
                continue
            print("{:d}: {:s}".format(i, sys.argv[i]))
