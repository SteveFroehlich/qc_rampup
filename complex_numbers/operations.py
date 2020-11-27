"""
    Data structures and implementations for
    complex operations
"""
import decimal
from decimal import Decimal

# Set precision to a fixed value
decimal.getcontext().prec = 10


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imag = imaginary_part

    def add(self, other):
        # add real and imaginary components
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def mult(self, other):
        """
            (a + bi) * (c + di)
            a*c + a*di + bi*c + bi*di
        """
        real = self.real * other.real
        imag = -1 * self.imag * other.imag
        mix = (self.real * other.imag) + (self.imag * other.real)
        real = real + imag
        return ComplexNumber(real, mix)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def divide(self, other):
        """
            use to formula for division
            c1 = a1 + b1
            c2 = a2 + b2
            c1/c2 = (a1*a2 + b1*b2)/(a2 + b2) + (a2*b1 + a1*b2)/(a2 + b2)i

            Values are wrapped in Decimal to control precision and avoid
            loss due to floating point arithmetic. They are converted back
            to float to be consistent with test values for assertions
        """
        denominator = Decimal(other.real**2 + other.imag**2)
        real = Decimal(self.real*other.real + self.imag*other.imag)/denominator
        imag = Decimal(other.real*self.imag - self.real*other.imag)/denominator
        return ComplexNumber(float(real), float(imag))


def csv_to_number():
    file_name = "numbers.csv"
    data = []
    with open(file_name) as file:
        for line in file.readline():
            left, right = line.split(",")
            real, op, imag = left.split(" ")
            cmplx_lt = ComplexNumber(real, imag)

            real, op, imag = right.split(" ")
            cmplx_rt = ComplexNumber(real, imag)
            entry = [cmplx_lt, cmplx_rt]
            data.append(entry)
    return data


def main():
    # read in csv of numbers
    # iterate through calling operation and saving result in list
    # output list of results
    pass


if __name__ == "__main__":
    main()
