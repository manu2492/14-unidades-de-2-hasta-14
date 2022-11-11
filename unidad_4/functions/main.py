import logging as log
import logging.config


# logging config
log.config.fileConfig(
    'log_config_file.conf'
)

logger = log.getLogger("main")


try:

    logger.info("...Leyendo el archivo...")
    # open the file
    file = open("functions/cuento.txt", 'r')
    logger.info("...Archivo procesado...")

except OSError:
    logger.error("No se pudo abrir el archivo", exc_info=True)
