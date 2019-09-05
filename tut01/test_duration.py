#!/usr/bin/env python3
# vim: textwidth=80 tabstop=4 shiftwidth=4 expandtab:

import sys
import traceback

### helpers ####################################################################

EPSILON = 1e-7

def are_close(m, n):
    return abs(m - n) < EPSILON

### test cases #################################################################

def test01():
    return elapsed_minutes("1234", "1234") == 0

def test02():
    return elapsed_minutes("0001", "0002") == 1

def test03():
    return elapsed_minutes("0237", "0337") == 60

def test04():
    return elapsed_minutes("0237", "0338") == 61

def test05():
    return elapsed_minutes("0959", "1058") == 59

def test06():
    return elapsed_minutes("0000", "2359") == 1439

def test07():
    return elapsed_minutes("1213", "1929") == 436

### reporting in technicolour ##################################################

def oops():
    return "\033[33mfailed\033[m"

def facepalm():
    return "\033[31mcrashed\033[m"

def yay():
    return "\033[32mpassed\033[m"

### test runner ################################################################

if __name__ == "__main__":
    try:
        from duration import elapsed_minutes
    except Exception as e:
        etype, eobj, etb = sys.exc_info()
        print("import:\t", oops(), "--", e, "@ line", etb.tb_lineno)
        print("Skipping further testing ...")
        quit()
    else:
        print("import:\t", yay())
    thismodule = sys.modules[__name__]
    testnames = [ x for x in dir() if x.startswith("test") ]
    tests = [ (x, getattr(thismodule, x)) for x in testnames ]
    for name, test in tests:
        try:
            if test():
                print(name + ":\t", yay())
            else:
                print(name + ":\t", oops())
        except Exception as e:
            etype, eobj, etb = sys.exc_info()
            topline = traceback.extract_tb(etb)[-1][1]
            print(name + ":\t", facepalm(), "--", e, "@ line", topline)
