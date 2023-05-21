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
                num_2 = float(input("Enter second number: "))
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
                print("Result = ", answer)
#try again feature
                while True:
                    again = input("Do you want to use the calculator again? (yes/no): ")
                    if again in ["Y", "YES", "yes", "Yes", "y", "N", "NO", "no", "No", "n"]:
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                if again in ["N", "NO", "no", "No", "n"]:
                    print("Thank you for using the calculator!")
                    break
#exception handling for invalid inputs
            except ZeroDivisionError:
                print("Syntax Error. Cannot be divided by zero. Please try again!")
            except ValueError:
                print("INVALID INPUT! PLEASE ENTER A NUMBER")