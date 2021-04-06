"""
Lab 5, exercise 2: Use gene expression data to create a classifier for Luminal A/ lUminal B breast cancer subtypes
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex2.py

import pandas as pd
import scipy.stats as stats
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

def my_classification_report(y_true, y_pred):
    n_samples = len(y_true)
    TP, FP, TN, FN = 0, 0, 0, 0

    for i in range(n_samples): 
        if y_true[i]==y_pred[i]==1:
           TP += 1
        if y_pred[i]==1 and y_true[i]!=y_pred[i]:
           FP += 1
        if y_true[i]==y_pred[i]==0:
           TN += 1
        if y_pred[i]==0 and y_true[i]!=y_pred[i]:
           FN += 1

    recall = TP/(TP+TN)
    precision = TP/(TP+FP)
    accuracy = (TP+TN)/(TP+FP+TN+FN)
    f1_score = (2*TP)/(2*TP+FP+FN)
    print("* Personal implementation results:")
    print("Recall: ", recall)
    print("Precision: ", precision)
    print("Accuracy: ", accuracy)
    print("F1 score: ", f1_score)


if __name__ == "__main__":
    full_data = pd.read_csv("dataset_LUMINAL_A_B.csv")
    reduced_data = pd.read_csv("reduced_dataset.csv")

    X_full = full_data.loc[:, full_data.columns != 'l'].values
    y_full = full_data.loc[:, full_data.columns == 'l'].values
    print(X_full.shape)
    X_red = reduced_data.loc[:, reduced_data.columns != 'l'].values
    y_red = reduced_data.loc[:, reduced_data.columns == 'l'].values
    le = LabelEncoder()
    y_full =le.fit_transform(y_full)
    y_red = le.transform(y_red)
    print("Label Encoder classes: ", le.classes_)

    #divide in train and test set
    X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_full, y_full, test_size=0.3, random_state=1)
    X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_red, y_red, test_size=0.3, random_state=1)

    #standardize the data
    X_train_full = (X_train_full - X_train_full.mean())/X_train_full.std()
    X_test_full = (X_test_full - X_test_full.mean())/X_test_full.std()
    X_train_red = (X_train_red - X_train_red.mean())/X_train_red.std()
    X_test_red = (X_test_red - X_test_red.mean())/X_test_red.std()

    pca = PCA(n_components=70)
    # with 80 it gives the error:
    #   ValueError: n_components=80 must be between 0 and min(n_samples, n_features)=70 with svd_solver='full'
    X_train_full_pca = pca.fit_transform(X_train_full)
    X_test_full_pca = pca.transform(X_test_full)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train_full_pca, y_train_full.ravel())  
    y_test_predicted = knn.predict(X_test_full_pca)
    print("-----PERFORMANCE ON FULL DATASET-----")
    my_classification_report(y_test_full, y_test_predicted)
    print(classification_report(y_test_full, y_test_predicted))

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train_red, y_train_full.ravel())  
    y_test_predicted = knn.predict(X_test_red)
    print("-----PERFORMANCE ON REDUCED DATASET-----")
    my_classification_report(y_test_red, y_test_predicted)
    print(classification_report(y_test_red, y_test_predicted))
