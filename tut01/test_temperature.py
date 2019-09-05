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
    t = celsius_to_fahrenheit(0)
    return are_close(t, 32.0)

def test02():
    t = celsius_to_fahrenheit(100)
    return are_close(t, 212.0)

def test03():
    t = celsius_to_fahrenheit(0.04)
    return are_close(t, 32.072)

def test04():
    t = celsius_to_fahrenheit(-40)
    return are_close(t, -40)

### reporting in technicolour ##################################################

def oops():
    return '\033[33mfailed\033[m'

def facepalm():
    return '\033[31mcrashed\033[m'

def yay():
    return '\033[32mpassed\033[m'

### test runner ################################################################

if __name__ == '__main__':
    try:
        from temperature import celsius_to_fahrenheit
    except Exception as e:
        etype, eobj, etb = sys.exc_info()
        print('import:\t', oops(), '--', e, "@ line", etb.tb_lineno)
        print('Skipping further testing ...')
        quit()
    else:
        print('import:\t', yay())
    thismodule = sys.modules[__name__]
    testnames = [ x for x in dir() if x.startswith('test') ]
    tests = [ (x, getattr(thismodule, x)) for x in testnames ]
    for name, test in tests:
        try:
            if test():
                print(name + ':\t', yay())
            else:
                print(name + ':\t', oops())
        except Exception as e:
            etype, eobj, etb = sys.exc_info()
            topline = traceback.extract_tb(etb)[-1][1]
            print(name + ':\t', facepalm(), '--', e, "@ line", topline)
