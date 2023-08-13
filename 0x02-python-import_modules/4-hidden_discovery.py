#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    den = dir(hidden_4)
    for i in range(len(den)):
        if den[i][:2] != "__":
            print("{:s}".format(den[i]))
