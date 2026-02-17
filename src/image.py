class MisstructuredImageException(Exception):
    ...

class Image(object):
    def __init__(self, digit: int, data: list[list[int | float]]):
        for d in data:
            if not isinstance(d, list):
                raise MisstructuredImageException("The digit argument should be a list of lists, where each sub-list is a row.")
        self.data = data
        self.digit = digit
