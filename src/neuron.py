import math

class Neuron:
    def __init__(self):
        self.weight = 0
        self.bias = 0
        self.last_input = None
    def activation_function(self, x):
        return 1 / (1 + math.exp(-x))
    def forward(self, input):
        self.last_input = input
        return self.activation_function(self.weight * input + self.bias)