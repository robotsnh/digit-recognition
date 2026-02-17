import os.path, csv

class NotACSVFileException(Exception):
    ...

class CSVFile(object):
    __slots__ = ["path", "rows"]
    def __init__(self, path: str):
        if not os.path.isfile(path):
            raise FileNotFoundError
        if not path[-4:] == ".csv":
            raise NotACSVFileException
        self.path = path
        self.rows = []
        with open(self.path) as file:
            reader = csv.reader(file)
            for row in reader:
                self.rows.append(row)