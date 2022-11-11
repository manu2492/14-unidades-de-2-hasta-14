def main_function():
    """this function decides which operation to do

    :return: the operation output
    :rtype: string
    """
    # get the inputs
    try:
        main_input: list = list(input().split())
        number_a, operator, number_b = main_input
    except ValueError:
        print("please use espaces or select a correct format,"
              " the input should be like this example: '3 + 4'")
        return main_function()

    # check operators
    operators: list = ['+', '-', '*', '/']
    if main_input[1] not in operators:
        print("please use one of this operators: +, - , /, *")
        return main_function()

    try:
        number_a = float(number_a)
        number_b = float(number_b)
    except ValueError:
        print("please selct a float")
        return main_function()

    # select the operation
    if operator == '+':
        print(addition(number_a, number_b))
    elif operator == '-':
        print(subtraction(number_a, number_b))
    elif operator == '*':
        print(multiplication(number_a, number_b))
    elif operator == '/':
        if number_b == 0.0:
            print("second number must be != 0")
            return main_function()
        else:
            print(division(number_a, number_b))


# functions
def addition(number_a: float, number_b: float) -> float:
    return number_a + number_b


def subtraction(number_a: float, number_b: float) -> float:
    return number_a - number_b


def multiplication(number_a: float, number_b: float) -> float:
    return number_a * number_b


def division(number_a: float, number_b: float) -> float:
    return number_a / number_b


if __name__ == '__main__':
    main_function()
