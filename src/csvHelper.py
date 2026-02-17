import os.path

class CSVFile(object):
    __slots__ = ["path"]
    def __init__(self, path: str):
        if not os.path.isfile(path):
            raise FileNotFoundError
        self.path = path
