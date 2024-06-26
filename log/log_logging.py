import sys
sys.dont_write_bytecode = True
import logging

LOG_PATH = './log/log_db.txt'

def report(message:str, level:str):
    logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG, filemode='a', format='%(levelname)s %(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    if level == 'info':
        logging.info(message)
    elif level == 'debug':
        logging.debug(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)
    elif level == 'warning':
        logging.warning(message)    
    else:
        logging.debug(message)