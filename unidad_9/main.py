
vehicles = ['car', 'plane', 'boat', 'bike', 'bus']


def select_vehicle() -> str:
    """This function returns the customer selection

    Returns:
    -------
        str
            the customer selection
    """
    try:
        number: int = int(input("your options are:\n 0-car\n 1-plane\n"
                          " 2-boat\n 3-bike\n 4-bus\nselect a number: "))
        return f"{vehicles[number]} is an excellent decision"

    except ValueError:
        print("value error please select an integer number")
        return select_vehicle()

    except IndexError:
        print("Index error, select a number between 0 and 4 included")
        return select_vehicle()


if __name__ == '__main__':
    print(select_vehicle())
