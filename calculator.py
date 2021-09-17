from typing import Literal, Union

Number = Union[float, int]

menu = {
    "1": "addition",
    "2": "subtraction",
    "3": "multiplication",
    "4": "division",
    "5": "modulus",
}

symbols = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%"}


def get_operation() -> str:
    for key, val in menu.items():
        print(f"{key} - {val.capitalize()}")

    choice = input("Please choose: ")
    if choice not in menu.keys():
        print("Please choose from one of the following options.")
        return get_operation()
    else:
        return choice


def get_number() -> Number:
    potential_number = input("Choose a number: ")
    try:
        float(potential_number)
    except ValueError:
        print("Please input a valid number.")
        return get_number()

    number = float(potential_number)
    if number == int(potential_number):
        return int(potential_number)
    else:
        return float


def do_operation(num_1: Number, operation: Literal["1", "2", "3", "4", "5"], num_2: Number) -> Number:
    operations = {
        "1": "__add__",
        "2": "__sub__",
        "3": "__mul__",
        "4": "__truediv__",
        "5": "__mod__",
    }
    return getattr(num_1, operations[operation])(num_2)


if __name__ == "__main__":
    operation = get_operation()
    num_1 = get_number()
    num_2 = get_number()
    result = do_operation(num_1, operation, num_2)
    print(num_1, symbols[operation], num_2, "=", result)
