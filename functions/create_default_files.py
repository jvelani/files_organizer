import  os
import sys
sys.dont_write_bytecode = True
from log.log_logging import LOG_PATH

def create_default_files():
    if not os.path.isfile(LOG_PATH):
        open(LOG_PATH, 'w')