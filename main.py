from calculator import Calculator
from calculator2 import CalculatorTwo
from user_interface import UserInterface

calc = Calculator()
calc_2 = CalculatorTwo()
ui = UserInterface()

num_1 = ui.ask_input()
num_2 = ui.ask_input()
operation = ui.operation()

if operation == "+":
    answer = calc.add(num_1, num_2)
elif operation == "-":
    answer = calc.subtract(num_1, num_2)
elif operation == "*":
    answer = calc.multiply(num_1, num_2)
elif operation == "/":
    answer = calc.divide(num_1, num_2)
elif operation == "**":
    answer = calc_2.exponent(num_1, num_2)
else:
    print("Invalid input. Choose an operation by entering a valid symbol (+, -, *, /, **).")

ui.result_display(answer)
