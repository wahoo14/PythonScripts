import numpy as np

class neural_network(object):
	'''
	Want the initialization function to take in a list of numbers representing the 
	nodes size for each layer (with multiple potential hidden layers)
	https://repl.it/@shamdasani/DigitRecognition
	eg. [4,5,5,2] = [input, hidden1, hidden 2, output]
	'''
	
	def __init__(self, *args):
		#get dictionary of sizes
		self.sizes = args
		
		#generate weight matrices
		weights=[]
		for i in range(len(args)):
			if i < len(args)-1:
				tempWeight = np.random.randn(args[i], args[i+1])
				weights.append(tempWeight)
			else:
				pass
		self.weights = weights
		
	def forwardProp(self, X):
		if not self.sizes.index:
			return []
		elif self.sizes.index == 0:
			return self.sigmoid(np.dot(X, weight))
		else
			return self.sigmoid(np.dot(forwardProp(self-1), correspondingWeight))	
		
		
	def sigmoid(self, s):
		# activation function
		return 1/(1+np.exp(-s))

	def sigmoidPrime(self, s):
		#derivative of sigmoid
		return s * (1 - s)
	
		
