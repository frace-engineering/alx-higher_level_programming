#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return(res)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as err:
        print("Exception:", err, file=sys.stderr)
        return(None)
