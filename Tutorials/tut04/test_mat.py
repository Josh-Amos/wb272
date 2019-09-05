#!/usr/bin/env python3
# vim: textwidth=80 tabstop=4 shiftwidth=4 expandtab:

import ast
import inspect
import sys
import traceback

### helpers ####################################################################

EPSILON = 1e-7

def are_close(m, n):
    return abs(m - n) < EPSILON

def getmatrix(m, n):
    return [[i*n + j + 1 for j in range(n)] for i in range(m)]

def gettransposed(m, n):
    return [[j + 1 for j in range(i, n*m, n)] for i in range(n)]

def checkdim(A, m, n):
    if not isinstance(A, list):
        raise MatrixError('matrix type not a list')
    if len(A) != m:
        raise MatrixError('matrix row dimension != {}'.format(m))
    for i in range(len(A)):
        if not isinstance(A[i], list):
            raise MatrixError('matrix row {} not a list'.format(i))
        if len(A[i]) != n:
            raise MatrixError('matrix row {} dimension != {}'.format(i, n))
    return True

def checkeq(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != B[i][j]: return False
    return True

class MatrixError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

### test cases #################################################################

def test01():
    A = getmatrix(2, 2)
    A_T = matrix_transpose(A)
    return checkdim(A_T, 2, 2)

def test02():
    A = getmatrix(2, 2)
    B = getmatrix(2, 2)
    A_T = matrix_transpose(A)
    B_T = gettransposed(2, 2)
    checkdim(A_T, 2, 2)
    return checkeq(A_T, B_T)

def test03():
    A = getmatrix(4, 2)
    A_T = matrix_transpose(A)
    return checkdim(A_T, 2, 4)

def test04():
    A = getmatrix(4, 2)
    B = getmatrix(4, 2)
    A_T = matrix_transpose(A)
    B_T = gettransposed(4, 2)
    checkdim(A_T, 2, 4)
    return checkeq(A_T, B_T)

def test05():
    A = getmatrix(100, 100)
    A_T = matrix_transpose(A)
    return checkdim(A_T, 100, 100)

def test06():
    A = getmatrix(100, 100)
    B = getmatrix(100, 100)
    A_T = matrix_transpose(A)
    B_T = gettransposed(100, 100)
    checkdim(A_T, 100, 100)
    return checkeq(A_T, B_T)

def test07():
    A = getmatrix(100, 100)
    A_T = matrix_transpose(A)
    return checkdim(A_T, 100, 100)

def test08():
    A = getmatrix(137, 139)
    B = getmatrix(137, 139)
    A_T = matrix_transpose(A)
    B_T = gettransposed(137, 139)
    checkdim(A_T, 139, 137)
    return checkeq(A_T, B_T)

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
        from mat import matrix_transpose
    except Exception as e:
        etype, eobj, etb = sys.exc_info()
        print('import:', oops(), '--', e, '@ line', etb.tb_lineno)
        print('Skipping further testing ...')
        quit()
    else:
        print('import:', yay())
    thismodule = sys.modules[__name__]
    testnames = [ x for x in dir() if x.startswith('test') ]
    tests = [ (x, getattr(thismodule, x)) for x in testnames ]
    for name, test in tests:
        try:
            if test():
                print(name + ':', yay())
            else:
                print(name + ':', oops())
        except MatrixError as e:
            print(name + ':', oops(), '--', e)
        except Exception as e:
            etype, eobj, etb = sys.exc_info()
            topline = traceback.extract_tb(etb)[-1][1]
            print(name + ':', facepalm(), '--', e, '@ line', topline)
