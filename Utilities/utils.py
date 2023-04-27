import inspect
import logging
from openpyxl import Workbook, load_workbook

class Utils:
    def __init__(self):
        self.logger = self.custom_logger()


    def custom_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        fh = logging.FileHandler("../Logs/automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


    def read_xlsx(file_name, sheet):
        datalist = []
        try:
            wb = load_workbook(filename=file_name)
            sh = wb[sheet]
            row_ct = sh.max_row
            col_ct = sh.max_column
            # Starting the range from 2 because first row content the headers
            for i in range(2, row_ct + 1):
                row = []
                for j in range(1, col_ct + 1):
                    row.append(sh.cell(row=i, column=j).value)
                datalist.append(row)
            return datalist
        except FileNotFoundError:
            raise Exception(f"File not located: {file_name}")
