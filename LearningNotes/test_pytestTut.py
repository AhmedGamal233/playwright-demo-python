'''
https://github.com/AndyLPK247/tau-intro-to-pytest

https://automationpanda.com/2020/02/18/how-do-i-start-learning-python/

1- install python form web site or from berw
2- python --version or python3 --version
3- https://www.educative.io/answers/how-to-add-python-to-the-path-variable-in-mac
4-pip install pytest
Note :If you need to use the python3 command to run Python, then you might also need to use the pip3 command in lieu of pip. 
Using pip will install packages globally for the whole machine. However, it's typically a best practice to manage dependencies per project using virtual environments. 
5- mkdir projectfolder
    cd projectfolder/
    mkdir tests
    Note : Pytest does not require a directory named "tests" per se, but most Python projects use it as a conventional way to separate product code from test code.
6- make sure that your python file starts with test_filename.py or filename_test.py
7- make sure that your method also starts with test_methodName or methodName_test
6- to run tests ===> python -m pytest testfilename

When a test fails due to a failed assertion, the exception will be an assertion error. However, tests will fail for _any _unhandled exception type.


'''
import pytest
def test_assertAdd():
    assert 1+2==3
    
# any raised exception that is not handled within a test case

# pytest safely catches any and all unhandled exceptions, performs any cleanup, and moves on to the next test case. Exceptions for one test case won't affect other tests.

# How do we verify that a piece of code successfully raises an exception inside test case?

# pytest actually provides a construct for handling expected exceptions: "pytest.raises".(it’s like try and catch)

import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

# with is a special statement for automatically handling extra "enter" and "exit" logic for a caller. 

# commonly used for file input and output.

# For "pytest.raises", the "enter" logic makes the code catch any exceptions, and the "exit" logic asserts if the desired exception type was actually raised.

# "pytest.raises" also looks for an exception of a specific type. If the steps within the statement's body do not raise the desired exception, then it will raise an assertion error to fail the test.

# we can also verify attributes of the raised exception. Notice how the "with" statement stores the exception object as a variable named 'e'

# Patameterized tc
# —————————
# Used when we want to test can have different kinds of inputs and outputs. They may also have specific boundary cases that should be tested

# Values put at list of tuples
products = [
    (2, 3, 6),                    # postive integers
    (1, 99, 99),                  # identity
    (0, 99, 0),                   # zero
    (3, -4, -12),                 # positive by negative
    (-5, -5, 25),     	        # negative by negative
    (2.5, 6.7, 16.75)             # floats
]

import pytest
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
  assert a * b == product

# a and b for the inputs and product for the outputs(expected result)

# the inner function is the test case. The outer function is the decorator itself, and it will call the inner test case once per input tuple.

# -We can read values from external file like csv
# -We can pass nums or strings or any data type

# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-2-data-driven-tests/

# Test classes
# ———————

# any directory with a file named _init_.py is treated as a package, and any modules inside that package may be imported by other modules. 

# pytest does not require tests to be a package. In fact, making the "tests" directory a package may have unintended consequences with tools like tox

# Create a new module named test_accum.py under the tests directory. In this module, add import statements for pytest and for the new Accumulator class(need to be tested class)

import pytest
from stuff.accum import Accumulator

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0


def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10

# They construct an Accumulator object, they make calls to the Accumulator object, and they verify the counts of the Accumulator objects or else verify some error.
# This pattern is called "Arrange-Act-Assert". It is the classic three-step pattern for functional test cases.
# 	1.	Arrange assets for the test (like a setup procedure).
# 	2.	Act by exercising the target behavior.
# 	3.	Assert that expected outcomes happened.
# pytest can run tests from multiple modules in the same Python project

# Fixtures are special functions that pytest can call before test case functions

# We put object in fixutuee to avoid duplication 
# 1-
@pytest.fixture
def accum():
    return Accumulator()

# 2-

# Remove the object creation line accum = Accumulator() and add a parameter to the test function signature named accum.
# This is all we need to do to make this test case use this fixture.

def test_accumulator_init(accum):
    assert accum.count == 0


# How does the fixture work? It's pytest magic!
# When pytest discovers a test case function, it looks at the function's parameter list.
# If the function has parameters, then it will search for fixtures to match each parameter's name.

# pytest versus xUnit Frameworks

# Xunit family
# ——————-

# -Tests are written as classes instead of functions.
# -A test class has methods for individual test cases.
# -They also have setup and cleanup methods.
# When tests run, setup and cleanup methods are executed before and after each test case method individually.
# xUnit-style test classes provide a decent structure for automating tests but, in my opinion, they have inherent weaknesses.

# -A test class's setup and cleanup methods can be used only within that class. cannot be reused by other classes. Classes and their variables also require programmers to carefully manage state in between test phases.

# Pytest
# ———

# -pytest avoids the limitations of classes by structuring tests as functions.

# -Fixtures are simply the function-based way to handle setup and cleanup operations.

# -Fixtures can be used by any test function in any module, so they are universally shareable since they use dependency injection to share state, they protect tests against unintended side effects.

# ** If you want to share fixtures between multiple test modules, you can move it to a module in the "tests" directory named "conftest.py".

# Conftest modules share test code for pytest. The name of the module is important. Pytest will automatically pick up any fixtures here

# ***test case can also use multiple fixtures, just make sure each fixture has a unique name:

@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def accum2():
    return Accumulator()

def test_accumulator_init(accum, accum2):
    assert accum.count == 0

# ****fixtures can handle both setup _and _cleanup. If you use a yield statement instead of a return statement in a fixture.

@pytest.fixture
def accum():
    yield Accumulator()
    print("DONE-ZO!")

# Basically, everything before the fixture's yield statement will be the "setup" steps, and everything after the fixture's yield statement will be the "cleanup" steps.

# The fixture will resume execution after the yield statement when the test case function completes, regardless of whether or not the test passed.

# Important example

# https://hackmd.io/@jenc/SJYmGcKsK

# *** You can also change the scope of the fixture, or when the fixture is run. By default, the scope is set to "function", meaning that the fixture will run once for each function that needs it. However, if you change the scope to "session", then the fixture runs only one time for the entire test suite.(like before/after)suite

@pytest.fixture
def accum(scope="session"):
    return Accumulator()

# If multiple tests use the fixture, then the fixture will run only for the first test. pytest will then store its return value and simply inject the return value into each subsequent test that needs it.
# "Session" scope would not be appropriate for these Accumulator tests, but it would be appropriate for a fixture that needs to read data from an external file. Other scope levels include "class", "module", and "package".


# Pytest commands

# 1-you can always learn about pytest's available command line options by using the --help or -h option:

# python -m pytest --help

# 2-we run the tests with the --verbose option or -v, pytest prints more data

# python -m pytest -v

# 3-run our tests with the --quiet option or -q, pytest doesn't print the top banner or even the test modules.

# python -m pytest -q

# 4- By default, pytest will run all tests it finds, no matter how many failures happen.
# However, you might want to stop execution sooner.
# To stop running tests after one failure, use the --exitfirst or -x option.

# python -m pytest -x

# 5-To stop running tests after a certain number of failures, use the --maxfail argument and set it to however many failures you want

# python -m pytest --maxfail=1

# 6-Pytest includes an option that will generate a JUnit XML file for test results.
# Simply use --junit-xml and add a report file path like so:

# python -m pytest --junit-xml report.xml

# Configuration files => 

# pytest.ini
# ———————————
# there might be some options you want to set more permanently, especially when running tests in a Continuous Integration environment.
# Some options are not available directly through the command line either.
# Thankfully, you can create a configuration file for pytest to specify options in a file rather than on the command line.
# Pytest supports a few different file formats for configuration files.


# Whichever format you choose, be sure you follow appropriate conventions. Configuration files should be loaded in the project's root directory.
# pytest configuration files support many options.
# addopts is one of the most useful. It lets you set options directly as they would be entered on the command line.
# Several other options exist as well, so take time to review them on the pytest docs online.

# Create a new file named "pytest.ini" in the project root directory. Add the following lines and save the file:

# [pytest]
# junit_family = xunit2

# This option should make that JUnit XML warning message go away. Re-run the tests with the JUnit XML option.

# Filter tests
# —————-

# 1-run all of our tests because they all reside in the "tests" directory

# python -m pytest tests

# 2-To run specific file 

# python -m pytest tests/test_accum.py

# 3-run individual test case functions. To do this, supply the path to the module, followed by :: and the test case function name

# python -m pytest tests/test_math.py::test_one_plus_one

# 4-you may know a test name (or part of a test name) but you might not know its full module path.
# Or, you may want to run all tests that contain a certain token. To filter tests by such expressions, use the -k option. 

# python -m pytest -k Reg

# It supports boolean logic with "and", "or", and "not" keywords. For example:

# python -m pytest -k "one and not accum"

# -k is good 
# However, naming conventions are not always consistent,

# So we use 
# Markers
# ————-

# To add a marker to a test case function, add a "@pytest.mark" decorator, then add a suffix with a name for the marker. For example, let's add "@pytest.mark.accumulator"

@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0

# Whenever we add custom markers to pytest, we should also add them to the pytest configuration file. Otherwise, pytest will print warning messages.
# Make sure to open "pytest.ini" and add two new markers.

# [pytest]
# junit_family = xunit2
# markers =
#   accumulator
#   7mada
#   Regression
# testpaths = tests

# The command 

# python -m pytest -m accumelator

# also you can use "and", "or", and "not" boolean expressions with -m, 

# some of pytest's standard markers: 
# 	•	"skip" will skip the test case.
# 	•	"skipif" will skip the test case based on a given condition. For example, tests may not be applicable for certain operating systems or Python versions.
# 	•	"xfail" will report an expected failure if the test case fails. This helps avoid report pollution for known problems.
# 	•	"parameterize" we've already encountered in a previous chapter.
# ** By default, pytest will search for test cases either from the current directory or from the paths and options given at the command line.
# However, setting "testpaths" in the configuration file will explicitly set test case search paths.
# For example, we can set "testpaths = tests" in our pytest.ini file to make sure that pytest searches only the "test" folder.



# Plugins

# Html report plugin

# pip install pytest-html

# python -m pytest --html=report.html


# The "pytest-xdist" plugin lets you run pytest tests in parallel. 

# pip install pytest-xdist

# add the -n option with the number of threads to run. For example, -n 3 will run tests across three parallel threads.

# python -m pytest -n 3

# pytest-bdd