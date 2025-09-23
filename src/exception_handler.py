
import sys
import logging
from src.exception import custom_exception

def handle_exception(e: Exception):
    custom_error = custom_exception(e, sys)
    logging.error(str(custom_error))
    raise custom_error


# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         raise handle_exception(e)
    
