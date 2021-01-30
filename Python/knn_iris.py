"""
Author: Janith Weeraman
Date: 15/12/2020

Implementing the K-nearest neighbours algorithm on the Iris dataset
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Loading dataset into variables
iris = load_iris()
irisData = iris['data']
irisTargets = iris['target']
irisSpp = iris['target_names']

scalar = StandardScaler().fit(irisData)
# Scaling the iris
scaledIris = scalar.transform(irisData)

# adding and fitting in unknown plant data
testRec = np.array([[4.6, 3.0, 1.5, 0.2]])
plantRecs = np.array([[4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]])
scaledTest = scalar.transform(testRec)
scaledPlant = scalar.transform(plantRecs)

testData = scaledTest[:, :2]
sepalData = scaledIris[:, :2]


def findKNNeighbours(data, targets, testData, species, n_neighbours=2):
    """
    method to construct a K-Nearest Neighbour classifier and print out the indices, coordinates, class labels and the
    species labels for given test data

    :param data: training data to train the model
    :param targets: target labels corresponding to the training data
    :param testData: the unknown data to be tested on
    :param species: species target list according to how labels are coded
    :param n_neighbours:
    :return: None
    """
    knn = KNeighborsClassifier().fit(data, targets)

    for test in testData:
        print("Predicted species:")
        for i in knn.predict(testData):
            print(irisSpp[i], end='\n')
        print("Nearest Neightbours:")
        for n in knn.kneighbors([test], n_neighbors=n_neighbours)[1][0]:
            print("index:", n, end='\t')
            print("coordinates:", data[n], end='\t')
            tmp = knn.predict([data[n]])[0]
            print('label:', tmp, end='\t')
            print('species:', species[tmp])
    print()


def findProbabilities(training_data, targets, test_data,species, n_neighbours=5):
    """
    Method to construct a K-Nearest Neighbor classifier and then run some test data over it and print out the
    cluster labels, the species labels and the probabilities for each data point

    :param training_data: training data to train the model
    :param targets: target labels corresponding to the training data
    :param test_data: the unknown data to be tested on
    :param species: species target list according to how labels are coded
    :param n_neighbours:
    :return:
    """
    knn = KNeighborsClassifier(n_neighbors=n_neighbours).fit(training_data, targets)
    print("Predictions:")
    for pred_species, pred_probability in zip(knn.predict(test_data),
                                              knn.predict_proba(test_data)):
        print(pred_species, end='\t')
        print(species[pred_species], end='\t')
        print(f'(probability: {pred_probability})')
    print('\n')


# Training KNN model using only sepal data and use it to find 2 nearest neighbours
print("Sepal data:\n")
findKNNeighbours(sepalData, irisTargets, testData, irisSpp, 2)

# Training sepal model for 5 nearest neighbours and
# Predicting the species of the unknown plants and their probabilities
testDataPlant = scaledPlant[:, :2]
findProbabilities(sepalData, irisTargets, testDataPlant,irisSpp)

# Training model using only Petal Data and use iti to find 2 nearest neighbours
petalData = scaledIris[:, 2:]
testDataPetal = scaledTest[:,2:]
testDataPlantPetal = scaledPlant[:, 2:]
print("Petal data:\n")
findKNNeighbours(petalData, irisTargets, testDataPetal, irisSpp)

# Training petal model for 5 nearest neighbours and
# Predicting the species of the unknown plants and their probabilities
testDataPlant = scaledPlant[:, 2:]
findProbabilities(sepalData, irisTargets, testDataPlantPetal,irisSpp)

# Training model for both sepal and petal data and carrying out predictions on test
# data as well as on the unknown plant data
print("Combined data: \n")
findKNNeighbours(irisData,irisTargets,scaledTest,irisSpp)
findProbabilities(irisData,irisTargets,scaledPlant,irisSpp)