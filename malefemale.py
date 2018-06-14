from sklearn import tree

# features
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 59, 37], [171, 75, 42], [181, 85, 43]]

# labels
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# DecisionTreeClassifier() initializes model as our classifier
model = tree.DecisionTreeClassifier()

# fit() trains the model on our data, enabling it to make predictions
model = model.fit(X, Y)


# ask for user input
print("Enter 3 parameters to predict gender: ")
params = list()

for i in range(3):
	n = input("Enter parameter {}: ".format(i+1))
	params.append(int(n))

# the predict() method will use the model to guess the class of the input
# prediction = model.predict([[190, 70, 43]])
prediction = model.predict([params])

print("Prediction: {}".format(prediction))
