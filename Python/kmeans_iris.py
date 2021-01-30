"""
Author: Janith Weeraman
Date: 15/12/2020

Implementing the K-means algorithm on the Iris dataset
"""

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Reading modified Iris dataset
iris_data = pd.read_csv('iris.csv')
# Getting sepal length and width only
len_wid = pd.DataFrame(iris_data, columns=['sepal.length', 'sepal.width'])
# labels of dataset
labels = iris_data['variety']

# Fitting data onto a KMeans algorithm. clusters = 3
km = KMeans(n_clusters=3).fit(len_wid)

kmLabels = km.labels_


def target_to_label(kmLabels, labels):
    """
    Method to take in cluster labels and and data labels and find which cluster matches which label.
    In the case of misalignments, the label that is most used for a cluster is assigned as the cluster label.

    Returns a dict with cluster numbers as keys and corresponding labels as values

    :param kmLabels:
    :param labels:
    :return dict:
    """
    # Temporary variables to hold data for processing
    index = {}
    holder = set(labels)
    lbls = {}

    # Create an empty dict as the value for each label key of index dict
    for var in holder:
        index[var] = {}

    # Count how many times each label is asigned to a particular cluster
    for label, species in zip(kmLabels, labels):
        index[species][label] = index.get(species).get(label, 0) + 1

    # For each label
    for i, j in index.items():
        # Find the cluster into which most of the points fell into
        values = list(j.values())
        cluster = list(j.keys())[values.index(max(values))]

        # Assign the label and cluster into a dictionary
        lbls[cluster] = i.lower()

    return lbls


def draw_diagram(xs, ys, labels, target2label, centers, data):
    # Dictionaries holding the different states and colors for different points in the graphs
    abbrs = {'setosa': 'St', 'virginica': 'Vg', 'versicolor': 'Vs'}
    colors = ['purple', 'blue', 'yellow']
    offsets = {'Vs': (0, 1.25), 'Vg': (1.75, 0), 'St': (-1.5, 0)}

    # Drawing a scatterplot of datapoints along with their clusters annoted
    for x, y, l in zip(xs, ys, labels):
        if l == 0:
            color = colors[l]
            text = abbrs[target2label[l]]
            offset = offsets[text]
            plt.scatter(x, y, c=color)
            plt.annotate(l, xy=(x, y))
            plt.annotate(text, xy=(x, y), xytext=(x + offset[0], y - offset[1]),
                         arrowprops=dict(color=color, linewidth=1, arrowstyle='->'))
        elif l == 1:
            color = colors[l]
            text = abbrs[target2label[l]]
            offset = offsets[text]
            plt.scatter(x, y, c=color)
            plt.annotate(l, xy=(x, y))
            plt.annotate(text, xy=(x, y), xytext=(x + offset[0], y - offset[1]),
                         arrowprops=dict(color=color, linewidth=1, arrowstyle='->'))
        else:
            color = colors[l]
            text = abbrs[target2label[l]]
            offset = offsets[text]
            plt.scatter(x, y, c=color)
            plt.annotate(l, xy=(x, y))
            plt.annotate(text, xy=(x, y), xytext=(x + offset[0], y - offset[1]),
                         arrowprops=dict(color=color, linewidth=1, arrowstyle='->'))

    # Drawing cluster centroids and unknown plants onto the same scatter plot
    # Centroids in red and unknowns in green
    plt.scatter(centers[:, 0], centers[:, 1], c='red')
    plt.scatter(data[:, 0], data[:, 1], c='green')
    plt.title("Modified Iris_data")


lbls = target_to_label(kmLabels, labels)

# Print the target integers along with their corresponding labels
print(lbls)
# Printing cluster centers
print("Cluster centers: ", km.cluster_centers_)

# Printing the predicted labels for the plants
plant = np.array([[4.6, 3.0], [6.2, 3.0]])
print("predicted label: ", km.predict(plant))
print()

draw_diagram(len_wid['sepal.length'], len_wid['sepal.width'], kmLabels, lbls, km.cluster_centers_, plant)
plt.savefig("modified_iris_sepal.jpg", dpi=300)
plt.close()

#

# Getting petal length and width only
len_wid = pd.DataFrame(iris_data, columns=['petal.length', 'petal.width'])

# Fitting data onto a KMeans algorithm. clusters = 3
km = KMeans(n_clusters=3).fit(len_wid)

kmLabels = km.labels_

lbls = target_to_label(kmLabels, labels)



# Print the target integers along with their corresponding labels
print(lbls)
# Printing cluster centers
print("Cluster centers: ", km.cluster_centers_)

# Printing the predicted labels for the plants
plant = np.array([[1.5,0.2],[4.1,1.2]])
print("predicted label: ", km.predict(plant))
print()

draw_diagram(len_wid['petal.length'], len_wid['petal.width'], kmLabels, lbls, km.cluster_centers_, plant)
plt.savefig("modified_iris_petal.jpg", dpi=300)
plt.close()
