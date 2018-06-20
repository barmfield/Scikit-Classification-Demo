This program will train 3 classifiers: a decision tree, support vector
machine, and and multi-layer perceptron network to make predictions about the
gender of an individual. Please note this is an overly simplistic model for
educational purposes, and is not intended to be representative of humans in
general. Training data was inspired by body statistics from the CDC (link
below).

Features (X): height, weight, shoe size

Label (Y): female, male


/----------RESULTS----------/
The decision tree model is the only one that selects correctly from user input
data. One major issue may be the limited number of examples. More exploration
is required to better understand the three models. 



The models are drawn from scikit-learn version 0.19.1.

A special thanks to Siraj Naval for the tutorial and inspiration (link below).

Sources/credit
--------------
Siraj Raval: https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A
CDC: https://www.cdc.gov/nchs/fastats/body-measurements.htm
Scikit-learn.org:
Tree: http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
SVM: http://scikit-learn.org/stable/modules/svm.html#classification
MLP: http://scikit-learn.org/stable/modules/neural_networks_supervised.html#neural-networks-supervised
