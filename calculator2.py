from calculator import Calculator

class CalculatorTwo(Calculator):
    def exponent(self, num_1, num_2):
        return num_1 ** num_2
    def divide(self, num_1, num_2):
        try:
            return num_1 / num_2
        except ZeroDivisionError:
            print("Syntax Error. Cannot be divided by zero. Please try again!")