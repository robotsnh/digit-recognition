class Image(object):
    def __init__(self, data: list[int]):
        self.data = data
        self.digit = data[0]