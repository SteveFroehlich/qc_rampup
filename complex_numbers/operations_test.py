"""
    Tests for each complex operation
    
    The tests follow the Given-When-Then
    structure of writing tests:
    https://en.wikipedia.org/wiki/Given-When-Then
"""
from pytest import approx
from operations import ComplexNumber
from operations import csv_to_number

# more info on float precision in the pytest.approx
# docs: https://docs.pytest.org/en/latest/reference.html#pytest-approx
FLOAT_PRECISION = 1e-4


def test_add():
    # given
    x = ComplexNumber(2, 5)
    y = ComplexNumber(7, 3)
    # when
    actual = x.add(y)
    # then
    expected = ComplexNumber(9, 8)
    assert_equal(expected, actual)


def test_multiply():
    x = ComplexNumber(4, 6)
    y = ComplexNumber(8, 9)
    expected = ComplexNumber(-22, 84)
    # when
    actual = x.mult(y)
    # then
    assert_equal(expected, actual)


def test_subtract():
    x = ComplexNumber(3, 5)
    y = ComplexNumber(14, 1)
    expected = ComplexNumber(-11, 4)
    # when
    actual = x.subtract(y)
    # then
    assert_equal(expected, actual)


def test_divide():
    # test data in divide.csv
    test_data = csv_to_number("divide.csv")
    for line in test_data:
        run_divide(line[0], line[1], line[2])


def run_divide(x, y, expected):
    print("running divide test with:")
    print("   x:        " + x.to_string())
    print("   y:        " + y.to_string())
    print("   expected: " + expected.to_string())
    print("")
    # when
    actual = x.divide(y)
    # then
    assert_equal(expected, actual)


def assert_equal(expected, actual):
    expected_real = approx(expected=expected.real, rel=FLOAT_PRECISION)
    expected_imag = approx(expected=expected.imag, rel=FLOAT_PRECISION)
    assert expected_real == actual.real
    assert expected_imag == actual.imag

test_divide()