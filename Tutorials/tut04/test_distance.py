#!/usr/bin/env python3
# vim: textwidth=79 tsbstop=4 shiftwidth=4 expandtab:

import ast
import inspect
import sys
import traceback

### helpers ####################################################################

EPSILON = 1e-7

def are_close(m, n):
    return abs(m - n) < EPSILON

class SourceChecker(ast.NodeVisitor):

    def __init__(self):
        self.has_ifs = False

    def found_ifs(self):
        return self.has_ifs

    def visit_If(self, node):
        self.has_ifs = True

def check_source(obj):
    source = inspect.getsource(obj)
    root = ast.parse(source)
    checker = SourceChecker()
    checker.visit(root)

    print('legal? ', end=' ')
    if checker.found_ifs():
        print(fingergun(), 'You used an if statement.')
        return False
    else:
        print(yay())
        return True

### test cases #################################################################

def test01():
    points = [(1, 0)]
    p, i, d = closest(points)
    return p == (1, 0) and i == 0 and are_close(d, 1)

def test02():
    points = [(1, 0), (2, 0)]
    p, i, d = closest(points)
    return p == (1, 0) and i == 0 and are_close(d, 1)

def test03():
    points = [(2, 0), (1, 0)]
    p, i, d = closest(points)
    return p == (1, 0) and i == 1 and are_close(d, 1)

def test04():
    points = [(2, 0), (-1, 0)]
    p, i, d = closest(points)
    return p == (-1, 0) and i == 1 and are_close(d, 1)

def test05():
    points = [(6.8, 8.3), (7.3, 8.5), (4.5, 3.6), (4.1, 4.7), (4.4, 7.7)]
    p, i, d = closest(points)
    return p == (4.5, 3.6) and i == 2 and are_close(d, 5.76281181369)

def test06():
    points = [(-3.2,  7.6), ( 2.0,  9.4), (7.3, 2.9), (2.1, -9.9),
              ( 5.7, -5.7), (-9.2, -1.2), (1.6, 6.1), (4.9,  5.9),
              (-6.4,  9.7), (-10.0, 1.6), (4.5, 7.0)]
    p, i, d = closest(points)
    return p == (1.6, 6.1) and i == 6 and are_close(d, 6.30634601017)

def test07():
    points = [(-7.06, -25.86), (-73.45, 15.98), (65.04, -5.54),
              (27.97, -97.28), (47.37, -35.79), (52.2, -87.23),
              (-40.29, 45.19), (59.36, 16.67), (39.4, 23.95), (36.16, -67.32),
              (-99.47, -87.75), (-73.9, 2.72), (22.61, -29.9), (-7.57, 49.61),
              (-33.24, 71.83), (-17.1, -70.81), (-79.56, 31.71), (22.71, 55.9),
              (-44.22, -82.9), (32.09, 91.92), (-22.21, 31.3), (51.56, -38.61),
              (-22.52, -91.14), (-80.75, -26.52), (92.1, 42.35), (-46.26,
              74.28), (-19.65, -13.2), (-99.48, 20.45), (-19.8, -0.21),
              (-56.07, 28.45), (80.97, 72.25), (92.85, 78.03), (23.22, 41.04),
              (-59.38, -13.0), (22.46, 49.48), (-62.01, 38.93), (-16.97,
              72.77), (-96.5, 16.75), (-17.66, -5.43), (-92.24, -94.0),
              (-71.16, 46.41), (59.58, 98.24), (25.68, 83.39), (49.2, 88.02),
              (38.96, -13.51), (62.47, -5.25), (31.47, -53.75), (6.03, -0.39),
              (-47.68, -53.36), (-84.53, -32.15), (70.7, -63.78), (61.28,
              -56.05), (-96.5, -75.1), (25.97, 90.13), (-70.13, -85.83),
              (10.65, -49.68), (86.49, 80.17), (-87.49, 0.45), (-58.84, 49.11),
              (-25.14, 97.97), (14.09, 32.6), (-88.87, 14.53), (87.94, -57.99),
              (-93.58, 20.12), (78.2, 75.99), (37.9, -4.08), (-13.18, 54.04),
              (27.48, 15.38), (42.62, -92.15), (8.76, -88.41), (29.74, -9.29),
              (-13.8, -72.93), (39.89, 49.72), (19.56, -77.17), (-31.27,
              47.67), (-33.49, -72.29), (-21.5, 68.62), (-6.42, -34.71),
              (-65.21, -14.91), (15.58, 62.9), (-11.34, 35.94), (56.07, 59.34),
              (13.15, 38.7), (50.6, 59.16), (70.44, -69.58), (-22.96, 77.47),
              (-43.3, 39.01), (-66.92, 17.81), (-26.52, 10.4), (40.21, 70.07),
              (83.75, -76.71), (32.99, -18.86), (-4.34, -75.2), (-16.82,
              -13.43), (-13.86, -16.32), (-82.4, -67.51), (88.65, -57.29),
              (-49.48, -22.66), (77.49, -46.71), (53.39, -10.63), (-57.88,
              -14.07), (-64.74, -82.89), (3.12, -24.48), (15.08, 46.49),
              (30.02, -71.7), (59.85, 95.4), (-68.14, 32.95), (18.63, -12.21),
              (28.91, -34.92), (-0.38, 2.34), (-2.09, -41.39), (49.24, -44.76),
              (67.99, -11.95), (84.66, 70.85), (89.38, 68.86), (90.16, 18.78),
              (52.15, 81.8), (47.32, 81.15), (39.13, -97.23), (4.05, 4.59),
              (64.79, 53.8), (68.63, -84.44), (2.86, -13.22), (54.63, -31.45),
              (-50.04, -3.12), (92.33, -88.11), (-67.64, -24.77), (-36.58,
              90.31), (80.51, 22.62), (3.09, 67.99), (-3.88, -60.31), (97.02,
              -65.65), (-83.56, 26.45), (71.48, 59.63), (-6.96, -1.78), (-5.48,
              -76.79), (-31.73, -97.86), (10.59, -96.23), (-79.98, -59.15),
              (10.95, 38.86), (-82.7, -59.06), (1.9, 91.64), (-78.69, 60.69),
              (-86.65, 69.64), (79.13, 60.87), (-65.43, 41.4), (-25.45,
              -97.62), (52.06, 81.53), (-40.64, 33.36), (26.12, -23.33)]
    p, i, d = closest(points)
    return p == (-0.38, 2.34) and i == 109 and are_close(d, 2.37065391823)

### reporting in technicolour ##################################################

def oops():
    return '\033[33mfailed\033[m'

def facepalm():
    return '\033[31mcrashed\033[m'

def fingergun():
    return '\033[31mHouston, we have a problem!\033[m'

def yay():
    return '\033[32mpassed\033[m'

### test runner ################################################################

if __name__ == '__main__':
    try:
        from distance import closest
    except Exception as e:
        etype, eobj, etb = sys.exc_info()
        print('import:', oops(), '--', e, "@ line", etb.tb_lineno)
        print('Skipping further testing ...')
        quit()
    else:
        print('import:', yay())
    if not check_source(closest):
        print('Skipping further testing ...')
        quit()
    thismodule = sys.modules[__name__]
    testnames = [ x for x in dir() if x.startswith('test') ]
    tests = [ (x, getattr(thismodule, x)) for x in testnames ]
    for name, test in tests:
        try:
            if test():
                print(name + ':', yay())
            else:
                print(name + ':', oops())
        except Exception as e:
            etype, eobj, etb = sys.exc_info()
            topline = traceback.extract_tb(etb)[-1][1]
            print(name + ':', facepalm(), '--', e, '@ line', topline)
