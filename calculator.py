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
                num_2 = float(input("Enter first number: "))
#if add, add 2 numbers
                answer = 0
                if operation == "+":
                    answer = self.add(num_1, num_2)
#if minus, subtract 2 numbers
                elif operation == "-":
                    answer = self.subtract(num_1, num_2)
#if multiply, multiply 2 numbers
                elif operation == "*":
                    answer = self.multiply(num_1, num_2)
#if divide, divide 2 numbers
                elif operation == "/":
                    answer = self.divide(num_1, num_2)
                else:
                    print("Invalid input. Choose an operation by entering a valid symbol (+, -, *, /).")
                    continue
#print output

#try again feature
#exception handling for invalid inputs