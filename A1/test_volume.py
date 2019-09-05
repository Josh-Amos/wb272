#!/usr/bin/env python3
# vim: textwidth=80 tabstop=4 shiftwidth=4 expandtab:

import ast
import builtins
import contextlib
import importlib
import inspect
import io
import signal
import sys
import textwrap
import traceback

### helpers ####################################################################

EPSILON = 1e-5


def are_close(m, n):
    """Test "equality" (closeness) of floating-point numbers."""
    return abs(m - n) < EPSILON


class File13(object):
    """Eat writes, acting as /dev/null."""
    def write(self, x):
        pass


class UnknownPromptError(Exception):
    """Exception class for an unknown prompt found during raw input capture."""

    def __init__(self, prompt):
        self._prompt = prompt

    def __str__(self):
        return 'Unknown raw_input prompt \'{}\''.format(self._prompt)


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
                if prompt.startswith(p) or p.startswith(prompt):
                    return self._prompt_to_response[p]
        raise UnknownPromptError(prompt)


@contextlib.contextmanager
def raw_input_capture(ric):
    """Capture raw_input."""
    saved_raw_input = builtins.raw_input
    builtins.raw_input = ric
    try:
        yield
    finally:
        builtins.raw_input = saved_raw_input


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
        raise TimeoutException('Timed out!')
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

### test cases #################################################################

def test01(tetrahedron_volume):
    '''tetrahedron_volume(0), which expects ~0.0'''
    t = tetrahedron_volume(0)
    return are_close(t, 0)

def test02(tetrahedron_volume):
    '''tetrahedron_volume(1.0), which expects ~0.11785'''
    t = tetrahedron_volume(1.0)
    return are_close(t, 0.11785)

def test03(tetrahedron_volume):
    '''tetrahedron_volume(1), which expects ~0.11785'''
    t = tetrahedron_volume(1)
    return are_close(t, 0.11785)

def test04(tetrahedron_volume):
    '''tetrahedron_volume(10), which expects ~117.85113'''
    t = tetrahedron_volume(10)
    return are_close(t, 117.85113)

def test05(tetrahedron_volume):
    '''tetrahedron_volume(113), which expects ~170047.04221'''
    t = tetrahedron_volume(113)
    return are_close(t, 170047.04221)

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
    return ANSI_COLOR['cyan'](function.__doc__)

### check source ###############################################################

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
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, None)
        if visitor:
            return visitor(node)
        else:
            self._visited.add(node.__class__.__name__)
            return self.generic_visit(node)

    def visit_Call(self, node):
        self._visited.add(node.__class__.__name__)

        # record callables
        callable_name = None
        if isinstance(node.func, ast.Attribute):
            # function
            callable_name = node.func.attr
        elif isinstance(node.func, ast.Name):
            # method
            callable_name = node.func.id
        if callable_name:
            self._callables.add(callable_name)

        # follow the name definition if defined in this module
        if callable_name in self._module_dir:
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

    # generate report
    report = []
    if len(toxic_statements) > 0:
        report.append('You used {}.'.format(', '.join(stmt for stmt in
                      sorted(toxic_statements))))
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
            if test(fts.function):
                print('{}:\t{}'.format(name, yay()))
            else:
                print('{}:\t{} on {}'.format(name, oops(), doc(test)))
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
    mts = ModuleTestSetup('volume.py')
    fts = FunctionTestSetup(mts, 'tetrahedron_volume', 'test')
    fts.set_illegal_statements(['For', 'If', 'Slice', 'While'])
    fts.set_illegal_calls(['index', 'find', 'sort', 'sorted'])
    return mts

### main #######################################################################

def main():
    # set up the tests
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
            if ((len(fts.illegal_statements) > 0 or len(fts.illegal_calls > 0))
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
