'''
David Fuller

Activation functions for a Neural Network.

2018-4-14
'''

import math


class ActivationFunction:
    def __init__(self, function, d_function):
        self.function = function
        self.d_function = d_function


# Sigmoid and derivative of sigmoid
sigmoid = ActivationFunction(lambda x: 1 / (1 + math.exp(-x)),
                             lambda y: y * (1 - y))

# Tanh and derivative of tanh
tanh = ActivationFunction(lambda x: math.tanh(x),
                          lambda y: 1 - (y * y))

# ReLU and derivative of ReLU
relu = ActivationFunction(lambda x: x * (x > 0),
                          lambda y: 1. * (y > 0))
