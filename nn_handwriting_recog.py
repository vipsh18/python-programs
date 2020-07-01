import numpy as np
import mnist_loader

class NeuralNetwork:
	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

	@staticmethod
	def sigmoid(x):
		return 1.0 / (1.0 + np.exp(-x))

	def sigmoid_derivative(self, x):
		return self.sigmoid(x) * (1 - self.sigmoid(x))

	@staticmethod
	def cost_derivative(output_activations, y):
		return output_activations - y

	def feedforward(self, a):
		for b, w in zip(self.biases, self.weights):
			a = self.sigmoid(np.dot(w, a) + b)
		return a

	def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
		n = len(training_data)
		if test_data: n_test = len(test_data)
		for i in range(epochs):
			np.random.shuffle(training_data)
			mini_batches = [training_data[k:k + mini_batch_size] for k in range(0, n, mini_batch_size)]
			for mini_batch in mini_batches:
				self.update_mini_batch(mini_batch, eta)
			if test_data:
				print(f"Epoch {i}: {self.evaluate(test_data)} / {n_test}")
			else:
				print(f"Epoch {i} complete")

	def update_mini_batch(self, mini_batch, eta):
		"""update network's weights and biases using gradient descent by applying backprop to a single mini_batch"""
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]
		for x, y in mini_batch:
			delta_nabla_b, delta_nabla_w = self.backprop(x, y)
			nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
			nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
		self.biases = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]
		self.weights = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]

	def backprop(self, x, y):
		"""return nabla_b, nabla_w representing gradient for cost_function c(x)"""
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]
		# feedforward
		activation = x
		activations = [x]
		zs = []
		for b, w in zip(self.biases, self.weights):
			z = np.dot(w, activation) + b
			zs.append(z)
			activation = self.sigmoid(z)
			activations.append(activation)
		# backward pass
		delta = self.cost_derivative(activations[-1], y) * self.sigmoid_derivative(zs[-1])
		nabla_b[-1] = delta
		nabla_w[-1] = np.dot(delta, activations[-2].T)
		for i in range(2, self.num_layers):
			z = zs[-i]
			sp = self.sigmoid_derivative(z)
			delta = np.dot(self.weights[-i+1].T, delta) * sp
			nabla_b[-i] = delta
			nabla_w[-i] = np.dot(delta, activations[-i-1].T)
		return nabla_b, nabla_w

	def evaluate(self, test_data):
		"""return the number of inputs for which the network outputs correct result"""
		test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
		return sum(int(x == y) for (x, y) in test_results)

if __name__ == "__main__":
	training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
	net = NeuralNetwork([784, 30, 10])
	net.SGD(training_data, 30, 10, 3.0, test_data=test_data)