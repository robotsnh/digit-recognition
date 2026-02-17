from csvHelper import CSVFile
from image import Image

class Dataset(object):
    __slots__ = ["rows", "images"]
    def __init__(self, dataFile: CSVFile):
       self.rows = dataFile.rows
       self.images = []

       for image in self.rows:
           self.images.append(Image(image))
