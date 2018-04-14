import random

from neuralnetwork import NeuralNetwork


xor_training_data = [
    {
        'inputs': [0, 1],
        'outputs': [1]
    },
    {
        'inputs': [1, 0],
        'outputs': [1]
    },
    {
        'inputs': [1, 1],
        'outputs': [0]
    },
    {
        'inputs': [0, 0],
        'outputs': [0]
    }
]

network = NeuralNetwork(input_nodes=2,
                        hidden_nodes=4,
                        output_nodes=1)

for i in range(20000):
    index = random.randint(0, len(xor_training_data) - 1)
    data = xor_training_data[index]
    network.train(data['inputs'], data['outputs'])

print('[0, 0]:', '{:.3f}'.format(network.predict([0, 0])[0]))
print('[0, 1]:', '{:.3f}'.format(network.predict([0, 1])[0]))
print('[1, 0]:', '{:.3f}'.format(network.predict([1, 0])[0]))
print('[1, 1]:', '{:.3f}'.format(network.predict([1, 1])[0]))
