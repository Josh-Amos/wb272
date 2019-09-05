#!/usr/bin/env python3
# vim: textwidth=80 tabstop=4 shiftwidth=4 expandtab:

import sys
import traceback

### helpers ####################################################################

EPSILON = 1e-7

def are_close(m, n):
    return abs(m - n) < EPSILON

### test cases #################################################################

def test00():
    return day_of_the_week(1961, 8, 13) == 0

def test01():
    return day_of_the_week(2013, 3, 11) == 1

def test02():
    return day_of_the_week(2013, 12, 31) == 2

def test03():
    return day_of_the_week(2012, 2, 29) == 3

def test04():
    return day_of_the_week(1989, 11, 9) == 4

def test05():
    return day_of_the_week(1900, 1, 5) == 5

def test06():
    return day_of_the_week(2009, 2, 7) == 6

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
        from days import day_of_the_week
    except Exception as e:
        etype, eobj, etb = sys.exc_info()
        print("import:\t", oops(), "--", e, '@ line', etb.tb_lineno)
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
