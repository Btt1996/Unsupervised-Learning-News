import logging

class Logging:
    def __init__(self):
        logging.basicConfig(filename='unsupervised_learning.log', level=logging.INFO)
    
    def log_info(self, message):
        logging.info(message)
    
    def log_error(self, message):
        logging.error(message)
    
    def log_warning(self, message):
        logging.warning(message)
    
    def log_critical(self, message):
        logging.critical(message)
    
    def log_debug(self, message):
        logging.debug(message)
