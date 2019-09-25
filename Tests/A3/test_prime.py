#!/usr/bin/env python3

import ast
import builtins
import contextlib
import inspect
import importlib
import io
import math
import random
import signal
import sys
import textwrap
import traceback

### helpers ####################################################################

EPSILON = 1e-13


def are_close(m, n):
    """Test "equality" (closeness) of floating-point numbers."""
    return abs(m - n) < EPSILON


class File13(object):
    """Eat writes, acting as /dev/null."""
    def write(self, x):
        pass


class UnknownPromptError(Exception):
    """Exception class for an unknown prompt found during input capture."""

    def __init__(self, prompt):
        self._prompt = prompt

    def __str__(self):
        return 'Unknown input prompt \'{}\''.format(self._prompt)


class TestError(Exception):
    """Exception class for test case errors."""
    pass


class TimeoutException(Exception):
    """Exception class for a timeout."""
    pass


class FunctionTestSetup(object):
    """Setup for functions to be tested."""

    def __init__(self, mts, fnname, test_fnname_start):
        self.blacklist = set()
        self.module_test_setup = mts
        mts.add_function_setup(self)
        self.fnname = fnname
        self.function = None
        self.illegal_calls = set()
        self.illegal_statements = set()
        self.legal_calls = set()
        self.test_fnname_start = test_fnname_start
        self.whitelist = set()

        # collect tests
        test_names = [x for x in dir(mts.mod)
                      if x.startswith(test_fnname_start)]
        self.tests = [(x, t) for x, t in [(y, getattr(mts.mod, y))
                      for y in test_names] if callable(t)]

    def set_illegal_calls(self, illegal_calls):
        self.illegal_calls = set(illegal_calls)

    def set_illegal_statements(self, illegal_statements):
        self.illegal_statements = set(illegal_statements)

    def set_legal_calls(self, legal_calls):
        self.legal_calls = set(legal_calls)

    def set_module_blacklist(self, blacklist):
        self.blacklist = set(blacklist)

    def set_module_whitelist(self, whitelist):
        self.whitelist = set(whitelist)

    def set_function(self, function):
        self.function = function


class ModuleTestSetup(object):
    """Setup for the module to be tested."""

    def __init__(self, filename):
        self.filename = filename
        self.function_setups = []
        self.modname = filename.split('.')[0]
        self.mod = sys.modules[__name__]

    def add_function_setup(self, function_setup):
        self.function_setups.append(function_setup)


class RawInputCapture(object):
    """Redirect raw_input to a challenge/response callable object."""

    def __init__(self, prompt_to_response):
        self._prompt_to_response = prompt_to_response

    def __call__(self, prompt=''):
        if prompt in self._prompt_to_response:
            return self._prompt_to_response[prompt]
        else:
            for p in self._prompt_to_response:
                if (prompt.startswith(p) or prompt != '' and
                        p.startswith(prompt)):
                    return self._prompt_to_response[p]
        raise UnknownPromptError(prompt)


@contextlib.contextmanager
def raw_input_capture(ric):
    """Capture raw_input."""
    saved_raw_input = builtins.input
    builtins.input = ric
    try:
        yield
    finally:
        builtins.input = saved_raw_input


@contextlib.contextmanager
def output_capture():
    """Capture stdout and stderr."""
    saved_stdout = sys.stdout
    saved_stderr = sys.stderr
    captured_outs = [io.StringIO(), io.StringIO()]
    sys.stdout, sys.stderr = captured_outs
    try:
        yield captured_outs
    finally:
        sys.stdout = saved_stdout
        sys.stderr = saved_stderr
        captured_outs[0] = captured_outs[0].getvalue()
        captured_outs[1] = captured_outs[1].getvalue()


@contextlib.contextmanager
def nostdout():
    """Context that prevents writing to the console via stdout.  Any exception
    reattaches stdout to the console."""
    saved_stdout = sys.stdout
    sys.stdout = File13()
    try:
        yield
    except Exception as e:
        sys.stdout = saved_stdout
        raise e
    sys.stdout = saved_stdout


@contextlib.contextmanager
def time_limit(seconds):
    """Apply a time limit to a context (e.g., a function) to prevent infinite
    loops."""
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

### test helper ################################################################

def run_test(f, param, *args, **kwargs):
    with nostdout(), time_limit(7):
        rval = f(param, *args, **kwargs)
    if rval == None:
        raise TestError('Your function did not return anything')
    return rval

### test cases #################################################################

def test01(prime_factorise):
    """prime_factorise(2)"""
    return sorted(prime_factorise(2)), [(2, 1)]

def test02(prime_factorise):
    """prime_factorise(3)"""
    return sorted(prime_factorise(3)), [(3, 1)]

def test03(prime_factorise):
    """prime_factorise(4)"""
    return sorted(prime_factorise(4)), [(2, 2)]

def test04(prime_factorise):
    """prime_factorise(5)"""
    return sorted(prime_factorise(5)), [(5, 1)]

def test05(prime_factorise):
    """prime_factorise(6)"""
    return sorted(prime_factorise(6)), [(2, 1), (3, 1)]

def test06(prime_factorise):
    """prime_factorise(7)"""
    return sorted(prime_factorise(7)), [(7, 1)]

def test07(prime_factorise):
    """prime_factorise(8)"""
    return sorted(prime_factorise(8)), [(2, 3)]

def test08(prime_factorise):
    """prime_factorise(9)"""
    return sorted(prime_factorise(9)), [(3, 2)]

def test09(prime_factorise):
    """prime_factorise(10)"""
    return sorted(prime_factorise(10)), [(2, 1), (5, 1)]

def test10(prime_factorise):
    """prime_factorise(11)"""
    return sorted(prime_factorise(11)), [(11, 1)]

def test11(prime_factorise):
    """prime_factorise(9739676404973)"""
    fcalc = run_test(prime_factorise, 9739676404973)
    fspec = [(17, 1), (572922141469, 1)]
    return sorted(fcalc), fspec

def test12(prime_factorise):
    """prime_factorise(170578732523501)"""
    fcalc = run_test(prime_factorise, 170578732523501)
    fspec = [(941, 1), (7121, 1), (25456241, 1)]
    return sorted(fcalc), fspec

def test13(prime_factorise):
    """prime_factorise(313837534462935)"""
    fcalc = run_test(prime_factorise, 313837534462935)
    fspec = [(3, 1), (5, 1), (7, 1), (53, 1), (5443, 1), (10360993, 1)]
    return sorted(fcalc), fspec

def test14(prime_factorise):
    """prime_factorise(444974544447988)"""
    fcalc = run_test(prime_factorise, 444974544447988)
    fspec = [(2, 2), (67, 1), (457, 1), (2503, 1), (1451521, 1)]
    return sorted(fcalc), fspec

def test15(prime_factorise):
    """prime_factorise(502374180165031)"""
    fcalc = run_test(prime_factorise, 502374180165031)
    fspec = [(31, 1), (1044737, 1), (15511673, 1)]
    return sorted(fcalc), fspec

def test16(prime_factorise):
    """prime_factorise(520554916536605)"""
    fcalc = run_test(prime_factorise, 520554916536605)
    fspec = [(5, 1), (29, 1), (3590033907149, 1)]
    return sorted(fcalc), fspec

def test17(prime_factorise):
    """prime_factorise(628712663608747)"""
    fcalc = run_test(prime_factorise, 628712663608747)
    fspec = [(628712663608747, 1)]
    return sorted(fcalc), fspec

def test18(prime_factorise):
    """prime_factorise(732617508978142)"""
    fcalc = run_test(prime_factorise, 732617508978142)
    fspec = [(2, 1), (366308754489071, 1)]
    return sorted(fcalc), fspec

def test19(prime_factorise):
    """prime_factorise(795074238419381)"""
    fcalc = run_test(prime_factorise, 795074238419381)
    fspec = [(564463, 1), (1408549787, 1)]
    return sorted(fcalc), fspec

def test20(prime_factorise):
    """prime_factorise(106896572092240000)"""
    fcalc = run_test(prime_factorise, 106896572092240000)
    fspec = [(2, 7), (5, 4), (7, 3), (3895647671, 1)]
    return sorted(fcalc), fspec


### reporting in technicolour ##################################################

ANSI_COLOR_LIST = [('black', 30), ('red', 31), ('green', 32), ('yellow', 33),
        ('blue', 34), ('magenta', 35), ('cyan', 36), ('white', 37)]


def ansi_color(ascii_code):
    def _cfunction(s):
        return '\033[{}m{}\033[m'.format(ascii_code, s)
    return _cfunction


ANSI_COLOR = {n:ansi_color(c) for n, c in ANSI_COLOR_LIST}


def oops():
    return ANSI_COLOR['yellow']('failed')


def facepalm():
    return ANSI_COLOR['red']('crashed')


def yay():
    return ANSI_COLOR['green']('passed')


def doh():
    return ANSI_COLOR['red']('Do\'h!')


def doc(function):
    return ANSI_COLOR['blue'](function.__doc__)

### check source ###############################################################

STATEMENT = {
    'Pow': 'the exponentiation operator'
}

class SourceVisitor(ast.NodeVisitor):
    """Explore the abstract syntax tree (AST) of a node."""

    def __init__(self, module=None):
        self._callables = set()
        self._imports = set()
        self._module = module
        self._module_dir = set(dir(module)) if module else []
        self._visited = set()

    def get_node_types(self):
        return self._visited

    def get_callables(self):
        return self._callables

    def get_illegal_statements(self):
        return self._illegals

    def get_imports(self):
        return self._imports

    def visit(self, node):
        name = node.__class__.__name__
        method_name = 'visit_' + name
        visitor = getattr(self, method_name, None)
        if visitor:
            return visitor(node)
        else:
            self._visited.add(name)
            return self.generic_visit(node)

    def visit_Call(self, node):
        self._visited.add(node.__class__.__name__)

        # record callables
        callable_name = None
        is_function = False
        if isinstance(node.func, ast.Attribute):
            # method
            callable_name = node.func.attr
        elif isinstance(node.func, ast.Name):
            # function
            callable_name = node.func.id
            is_function = True
        if callable_name:
            self._callables.add(callable_name)

        # follow the name definition if defined in this module
        if is_function and callable_name in self._module_dir:
            call = getattr(self._module, callable_name)
            source = inspect.getsource(call)
            root = ast.parse(source)
            checker = SourceVisitor(self._module)
            checker.visit(root)
            self._visited |= checker.get_node_types()
            self._callables |= checker.get_callables()

        # visit recursively
        self.generic_visit(node)

    def visit_Import(self, node):
        names = set([name.name for name in node.names])
        self._imports |= names
        self._visited.add('Import')

    def visit_ImportFrom(self, node):
        self._imports.add(node.module)
        self._visited.add('ImportFrom')


def has_legal_source(fts):
    """Checks whether the source of a function (sometimes module) is legal
    according to the function test setup."""
    module = sys.modules[fts.function.__module__]

    # visit function source
    source = inspect.getsource(fts.function)
    root = ast.parse(source)
    checker = SourceVisitor(module)
    checker.visit(root)

    # collect illegal (toxic) statements and calls
    toxic_statements = checker.get_node_types() & fts.illegal_statements
    toxic_calls = checker.get_callables() & fts.illegal_calls
    if len(fts.legal_calls) > 0:
        toxic_calls |= checker.get_callables() - fts.legal_calls
    toxic_modules = None

    # check module for imports
    imports = set(['Import', 'ImportFrom']) & fts.illegal_statements
    if len(imports) > 0 or len(fts.blacklist) > 0 or len(fts.whitelist) > 0:
        msource = inspect.getsource(module)
        mroot = ast.parse(msource)
        mchecker = SourceVisitor()
        mchecker.visit(mroot)
        if len(fts.blacklist) == 0 and len(fts.whitelist) == 0:
            toxic_statements |= mchecker.get_node_types() & imports
        else:
            toxic_modules = [m for m in mchecker.get_imports() if m not in
                    fts.whitelist or m in fts.blacklist]

    # check for loop
    # loops = set([
    #     'DictComp',
    #     'For',
    #     'GeneratorExp',
    #     'ListComp',
    #     'SetComp',
    #     'While',
    # ])
    # if len(loops & checker.get_node_types()) == 0:
    #     print(ANSI_COLOR['yellow']('WARNING -- no loop(s) found...'))

    # generate report
    report = []
    if len(toxic_statements) > 0:
        report.append('You used {}.'.format(', '.join(STATEMENT.get(stmt, stmt)
                      for stmt in sorted(toxic_statements))))
    if len(toxic_calls) > 0:
        report.append('You called {}.'.format(', '.join(call for call in
                      sorted(toxic_calls))))
    if toxic_modules:
        report.append('You imported illegal module{} {}.'.format('s' if
            len(toxic_modules) > 1 else '', ', '.join(m for m in
                sorted(toxic_modules))))

    # display report
    wrap = textwrap.TextWrapper(initial_indent='legal?  ',
            subsequent_indent='        ', width=80).wrap
    print('\n'.join(wrap(doh() + '  ' + '  '.join(report)
                    if len(report) > 0 else yay())))

    return len(report) == 0

### test runner ################################################################

def run_tests(fts, target_filename):
    for name, test in fts.tests:
        try:
            rvalue, expected = test(fts.function)
            if rvalue == expected:
                print('{}:\t{}'.format(name, yay()))
            else:
                print('{}:\t{} {}'.format(name, oops(), doc(test)))
                print('{}returned   {}\n{}instead of {}'.format(
                        ' '*8,
                        ANSI_COLOR['red'](rvalue),
                        ' '*8,
                        ANSI_COLOR['green'](expected)))
        except Exception as e:
            etype, eobj, etb = sys.exc_info()
            label = oops() if isinstance(e, TestError) else facepalm()
            print('{}:\t{} on {}'.format(name, label, doc(test)))
            print(' '*8 + etype.__name__ + ': ' + str(e))
            frames = traceback.extract_tb(etb)
            for fname, lineno, funcname, context in frames:
                if fname.endswith(target_filename):
                    print(' '*8 + 'line ' + str(lineno) + ': '+ context)

### test setup #################################################################

def set_up_tests():
    mts = ModuleTestSetup('prime.py')
    fts = FunctionTestSetup(mts, 'prime_factorise', 'test')
    fts.set_module_whitelist([
        'sys',
    ])
    return mts

### main #######################################################################

def main():
    mts = set_up_tests()

    # try to import the target module
    try:
        with nostdout():
            target_module = importlib.import_module(mts.modname)
    except Exception as e:
        etype, eobj, etb = sys.exc_info()
        print('import:', oops(), '--', e)
        formatted = traceback.format_exception_only(etype, eobj)
        if len(formatted) > 1:
            for context in formatted[1:-1]:
                print(context,)
        print('Skipping further testing ...')
        return -1
    else:
        print('import:', yay())

    # find the target function(s)
    red = ANSI_COLOR['red']
    targets = []
    for fts in mts.function_setups:
        try:
            function = getattr(target_module, fts.fnname)
        except AttributeError:
            print(red('Function \'{}\' is not defined'.format(fts.fnname)))
            continue
        if callable(function):
            fts.set_function(function)
            targets.append(fts)
        else:
            print(red('\'{}\' is not a function', fname))

    # check for legal source
    test_targets = []
    if len(targets) > 0:
        for fts in targets:
            if ((len(fts.illegal_statements) > 0 or len(fts.illegal_calls) > 0)
                    and not has_legal_source(fts)):
                print('Skipping further testing')
                continue
            test_targets.append(fts)
    else:
        print('Nothing to test ... stopping')
        return -1

    # run the tests
    for fts in test_targets:
        run_tests(fts, '/' + mts.filename)

    return 0


# run if invoked from the command line
if __name__ == '__main__':
    sys.exit(main())
