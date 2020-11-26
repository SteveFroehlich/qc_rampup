from operations import ComplexNumber


def test_add():
    # given
    x = ComplexNumber(2, 5)
    y = ComplexNumber(7, 3)
    # when
    actual = x.add(y)
    # then
    expected = ComplexNumber(9, 8)
    assert actual.real == expected.real
    assert actual.imag == expected.imag


def test_multiply():
    x = ComplexNumber(4, 6)
    y = ComplexNumber(8, 9)
    expected = ComplexNumber(-22, 84)
    # when
    actual = x.mult(y)
    # then
    assert expected.real == actual.real
    assert expected.imag == actual.imag


def test_subtract():
    x = ComplexNumber(3, 5)
    y = ComplexNumber(14, 1)
    expected = ComplexNumber(-11, 4)
    # when
    actual = x.subtract(y)
    # then
    assert expected.real == actual.real
    assert expected.imag == actual.imag
