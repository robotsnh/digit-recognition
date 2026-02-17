import math
from mathHelper import sigmoid

class Neuron:
    def __init__(self):
        self.weight = 0
        self.bias = 0
        self.last_input = None
    def forward(self, input):
        self.last_input = input
        return sigmoid(self.weight * input + self.bias)