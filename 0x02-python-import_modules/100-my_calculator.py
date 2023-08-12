#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, div, sub
    args = len(sys.argv) - 1
    result = 0
    if (args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] == "+"):
        result = a + b
        print("{:d} + {:d} = {:d}".format(a, b, result))
    elif (sys.argv[2] == "-"):
        result = a - b
        print("{:d} + {:d} = {:d}".format(a, b, result))
    elif (sys.argv[2] == "*"):
        result = a * b
        print("{:d} + {:d} = {:d}".format(a, b, result))
    elif (sys.argv[2] == "/"):
        result = a / b
        print("{:d} + {:d} = {:d}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
