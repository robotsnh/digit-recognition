class Neuron:
    def __init__(self):
        self.weight = 0
        self.bias = 0
        self.last_inputs = None
    def activation_function(self, x):
        return 1 / (1 + math.exp(-x))
    def forward(self, inputs):
        self.last_inputs = inputs
        self.outputs = []
        for i in inputs:
            i*=self.weight
            i+=self.bias
            self.outputs.append(activation_function(i))
        return self.outputs
