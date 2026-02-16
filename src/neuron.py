import math

class Neuron:
    def __init__(self):
        self.weight = 0
        self.bias = 0
        self.last_input = None
    def _sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    def forward(self, input):
        self.last_input = input
        return self._sigmoid(self.weight * input + self.bias)