import os, sys
from datetime import datetime 
import logging



def get_logger(name: str) -> logging.Logger:
    logger_name = f"{name}"
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
    )
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger