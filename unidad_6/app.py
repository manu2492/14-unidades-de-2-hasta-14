import logging

# logging config
logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s %(levelname)s:%(message)s',
                datefmt="%Y-%m-%dT%H:%M:%S%z"
)
log = logging.getLogger(__name__)


lista_inicial: list = ['perro', 'elefante', 'dragón']


# version 1
def len_chars(arr: list) -> list:
    """This function recibes "initial_list" and returns
       a list with the number of chars of each element

    :param arr: the list you want to measure
    :type arr: list
    :return: list with lenght of each item
    :rtype: list
    """
    len_list = []
    for i in arr:
        len_list.append(len(i))
    return len_list


# version 2
# This list receives "initial_list" and creates a list with the
# number of chars of each element
len_chars_comprehension_version: list = [len(x) for x in lista_inicial]

# version 3
# This list receives "initial_list" and creates a list with the
# number of chars of each element
len_chars_map_version: list = list(map(len, lista_inicial))


try:
    len_chars_2 = len_chars(lista_inicial)
    log.info(f"the output of 'len_chars_typing_version' is {len_chars_2}")
except Exception:
    log.error("len_chars_typing_version' function failed", exc_info=True)

log.info("the output of 'len_chars_comprehension_version' is" +
         f"{len_chars_comprehension_version}")

log.info(f"the output of 'len_chars_map_version' is {len_chars_map_version}")
