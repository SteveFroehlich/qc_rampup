
class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imag = imaginary_part

    def add(self, other):
        raise Exception("implement me")

    def mult(self, other):
        raise Exception("implement me")


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
    # iterate through calling mult and saving result in list
    # output list of results
    pass


if __name__ == "__main__":
    main()
