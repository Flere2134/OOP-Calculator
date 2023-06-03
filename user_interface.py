class UserInterface:
    def ask_input(self):
        while True:
            try:
                number = float(input('Enter a number: '))
                return number
            except ValueError:
                print("INVALID INPUT! PLEASE ENTER A NUMBER")
    def operation(self):
        operation = input("Enter operation symbol (+, -, *, /, **): ")
        return operation
    def result_display(self, answer):
        print("Result:", answer)