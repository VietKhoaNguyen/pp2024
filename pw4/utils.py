# pw4/utils.py
def input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid integer.")
