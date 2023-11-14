import logging


# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='my_log.log',
#     filemode='w',
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )


logger = logging.Logger("Logger")
logger.setLevel(20)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler(filename='my_log.log', mode='w')
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.info("start application")
s = 10
y = 1

try:
    res = s / y
    logger.info(f'Operation end: {res}')
except ZeroDivisionError as error:
    logger.error(f'Error{error}')
else:
    print(res)

logger.debug("debug info")
