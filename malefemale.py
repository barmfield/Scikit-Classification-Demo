from sklearn import tree
from sklearn import svm
from sklearn.neural_network import MLPClassifier as mlp

# features: height, weight, shoe size
X = [[70., 195., 10.], [73., 185., 11.], [63., 168., 7.], [60., 150., 8.], [65., 180., 9.], [73., 162., 11.], [65., 126., 7.], [63., 145., 7.], [62., 150., 9.], [68., 175., 9.], [66., 200., 12.]]

# labels
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# /-------------Decisiion Tree--------------/
# DecisionTreeClassifier() initializes tree_model as our classifier and
# fit() trains the model on our features and labels, enabling it to make 
# predictions
tree_model = tree.DecisionTreeClassifier()
tree_model = tree_model.fit(X, Y)


# /----------Support Vector Machine----------/
# SVC() initializes svm_model as a classifier and fit()
svm_model = svm.SVC()
svm_model = svm_model.fit(X, Y)


# /----------Multi-layer Perceptron---------/
mlp_model = mlp(solver='lbfgs', alpha=1e-5, 
				hidden_layer_sizes=(5, 2), random_state=1)
mlp_model = mlp_model.fit(X, Y)


# ask for user input
print("\nEnter height, weight, and shoe size to predict gender... ")
param_vals = list()
params = ['Height (in inches)', 'Weight', 'Shoe size']

while True:
	print()
	param_vals.clear()
	for param in params:
		n = input("{}: ".format(param))
		param_vals.append(float(n))

	# the predict() method will use the model to guess the class of the input
	# prediction = model.predict([[190, 70, 43]])
	tree_pred = tree_model.predict([param_vals])
	svm_pred = svm_model.predict([param_vals])
	mlp_pred = mlp_model.predict([param_vals])

	print("\nPrediction using decision tree: {}".format(tree_pred))
	print("Prediction using support vector machine: {}".format(svm_pred))
	print("Prediction using multi-layer perceptron: {}".format(mlp_pred))
	print()

	loop = input("Enter y to ask again...  ")
	if loop.lower() != "y":
		break
