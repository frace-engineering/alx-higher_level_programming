#!/usr/bin/python3
def main():
    pass

if __name__=="__main__":
    import sys
    nargs = len(sys.argv) - 1
    sum1 = 0
    for i in range(1, len(sys.argv)):
        sum1 += int(sys.argv[i])
    print("{:d}".format(sum1))
    main()
