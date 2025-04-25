import logging
import os
import datetime


class Logger:
    @staticmethod
    def get_logger(logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Reports', 'logs'))
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        log_file = os.path.join(logs_dir, f"{logger_name}_{timestamp}.log")

        # Create file handler
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger