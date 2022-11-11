from main import file
import logging as log
import logging.config
import os

# DIR = os.path.dirname(os.path.normpath(__file__))

# logging config
log.config.fileConfig(
    'log_config_file.conf'
)

# create logger
logger = log.getLogger("function")

# read file
content = file.read()
# split file into rows
rows = content.split("\n")


# count rows function
def count_rows():
    counter = 0
    for i in rows:
        counter += 1
    logger.info(f"cuento.txt - Cantidad de renglones: {counter}")


# count words function
def count_words():

    for i in range(len(rows)):

        words = rows[i].replace(",", "")
        words = words.replace(".", "")
        count = len(words.split(" "))
        logger.info(f"Renglón {i}: {count} palabras")


def main():
    count_rows()
    count_words()


if __name__ == '__main__':
    main()
