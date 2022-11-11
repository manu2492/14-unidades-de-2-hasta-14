import logging as log

fruits: list = ['Frutilla', 'Melón', 'PERA', 99.6, 'NaranJA', 'mORa', 'NisPERo', 99]

# logging config
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s %(message)s'
                )


def to_lower(arr: list) -> list:
    """return a list with each element lowercase

    :param arr: the list you want to convert to lowercase
    :type arr: list
    :return: lowercase list
    :rtype: list
    """
    lower_list = []
    for i in range(len(arr)):
        # if the item is string
        if type(arr[i]) == str:
            # item to lowercase
            new_item: str = arr[i].lower()
            log.info(f"conversión exitosa: {arr[i]}--->{new_item}")
            # add item to the new list
            lower_list.append(new_item)
        else:
            log.info(f"conversión fallida: ---> {arr[i]}")
            lower_list.append(arr[i])

    return lower_list


if __name__ == '__main__':
    to_lower(fruits)
