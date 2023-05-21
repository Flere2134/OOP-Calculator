class Calculator:
#method for addition
    def add(self, num_1, num_2):
        return num_1 + num_2
#method for subtraction
    def subtract(self, num_1, num_2):
        return num_1 - num_2
#method for multiplication
    def multiply(self, num_1, num_2):
        return num_1 * num_2
#method for division
    def divide(self, num_1, num_2):
        return num_1 / num_2
#method of main calculator
    def main(self):
        while True:
            try:
#ask user input 1st number
                num_1 = float(input("Enter first number: "))
#ask user input of operation
                operation = input("Enter operation symbol: ")
#ask user input 2nd number
#if add, add 2 numbers
#if minus, subtract 2 numbers
#if multiply, multiply 2 numbers
#if divide, divide 2 numbers
#print output
#try again feature
#exception handling for invalid inputs