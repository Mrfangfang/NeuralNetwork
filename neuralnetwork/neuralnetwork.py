'''
David Fuller

NeuralNetwork class: Template for a Neural Network object.

2018-1-11
'''

from .matrix import Matrix
from .activationfunctions import sigmoid, tanh


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        '''
        NeuralNetwork's init method.

        Sets up a neural network.

        Args:
            input_nodes (int): Number of nodes in input layer.
            hidden_nodes (int): Number of nodes in hidden layer.
            output_nodes (int): Number of nodes in output layer.
        '''

        if isinstance(input_nodes, NeuralNetwork):
            self.input_nodes = input_nodes.input_nodes
            self.hidden_nodes = input_nodes.hidden_nodes
            self.output_nodes = input_nodes.output_nodes

            self.weights_ih = input_nodes.weights_ih.copy()
            self.weights_ho = input_nodes.weights_ho.copy()

            self.hidden_bias = input_nodes.hidden_bias
            self.output_bias = input_nodes.output_bias
        else:
            self.input_nodes = input_nodes
            self.hidden_nodes = hidden_nodes
            self.output_nodes = output_nodes

            self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
            self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)

            self.weights_ih.randomize()
            self.weights_ho.randomize()

            self.hidden_bias = Matrix(self.hidden_nodes, 1)
            self.output_bias = Matrix(self.output_nodes, 1)
            self.hidden_bias.randomize()
            self.output_bias.randomize()

        self.set_learning_rate()
        self.set_activation_function(tanh)

    def set_learning_rate(self, learning_rate=0.1):
        '''
        Sets learning rate of neural network.

        Args:
            learning_rate (float): Learning rate to set. Defaulst to 0.1.
        '''

        self.learning_rate = learning_rate

    def set_activation_function(self, function=sigmoid):
        '''
        Sets activation function for Neural Network.

        Args:
            function (method): The activation function to use.
        '''

        self.activation_function = function

    def train(self, input_array, target_array):
        '''
        Computes outputs of hidden and output layers and trains Neural Network.

        Args:
            input_array (array): Array of network input values.
            target_array (array): Array of network target values.
        '''

        # Generate hidden outputs
        input_layer = Matrix.from_array(input_array)
        hidden_layer = Matrix.static_multiply(self.weights_ih, input_layer)
        hidden_layer.add(self.hidden_bias)
        hidden_layer = Matrix.map(
            hidden_layer, self.activation_function.function)

        # Generate output outputs
        output_layer = Matrix.static_multiply(self.weights_ho, hidden_layer)
        output_layer.add(self.output_bias)
        output_layer = Matrix.map(
            output_layer, self.activation_function.function)

        # Convert array to matrix object
        targets = Matrix.from_array(target_array)

        # Calculate error
        output_errors = Matrix.subtract(targets, output_layer)

        # Hidden to output weights - gradient descent
        gradients = Matrix.map(
            output_layer, self.activation_function.d_function)
        gradients.multiply(output_errors)
        gradients.multiply(self.learning_rate)
        hidden_t = Matrix.transpose(hidden_layer)
        delta_weights_ho = Matrix.static_multiply(gradients, hidden_t)

        # Adjust weights and bias
        self.weights_ho.add(delta_weights_ho)
        self.output_bias.add(gradients)

        # Hidden layer errors
        weights_ho_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.static_multiply(weights_ho_t, output_errors)

        # Calculate hidden gradients
        hidden_gradients = Matrix.map(
            hidden_layer, self.activation_function.d_function)
        hidden_gradients.multiply(hidden_errors)
        hidden_gradients.multiply(self.learning_rate)

        # Calculate input to hidden deltas
        inputs_t = Matrix.transpose(input_layer)
        delta_weights_ih = Matrix.static_multiply(hidden_gradients, inputs_t)

        # Adjust weights and bias
        self.weights_ih.add(delta_weights_ih)
        self.hidden_bias.add(hidden_gradients)

    def predict(self, input_array):
        '''
        Makes a prediction of what the output should be.

        Args:
            input_array (array): Array of network input values.

        Returns:
            array: Array of network output values.
        '''

        # Compute output of hidden layer
        input_layer = Matrix.from_array(input_array)
        hidden_layer = Matrix.static_multiply(self.weights_ih, input_layer)
        hidden_layer.add(self.hidden_bias)
        hidden_layer = Matrix.map(
            hidden_layer, self.activation_function.function)

        # Compute output of output layer
        output_layer = Matrix.static_multiply(self.weights_ho, hidden_layer)
        output_layer.add(self.output_bias)
        output_layer = Matrix.map(
            output_layer, self.activation_function.function)

        return output_layer.to_array()
