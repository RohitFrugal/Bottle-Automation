import inspect
import logging


class Utils:

    def __init__(self):
        self.logger = self.custom_logger()

    def assert_verifyItems(self, items, value):
        assert items.text == value
        print("assert pass")

    def custom_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        fh = logging.FileHandler("../Logs/automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger
