class UserInterface:
    def ask_input(self):
        number = float(input('Enter a number: '))
        return number
    def operation(self):
        operation = input("Enter operation symbol (+, -, *, /, **): ")
        return operation
    def result_display(self, answer):
        print(answer)