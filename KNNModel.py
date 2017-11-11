import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import ReadAndCreateDic as reader
import FindMode 
import pickle
from sklearn import preprocessing, cross_validation, svm, neighbors
from sklearn.linear_model import LinearRegression
import numpy as np

data = reader.getData()

X = np.array(data[['MILT_TIME', 'LATITUDE', 'LONGITUDE']])
y = np.array(data['PRIMARY_CAUSE_CD'])
 

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array(X_train[0])
example_measures = example_measures.reshape(1, -1)
prediction = clf.predict(example_measures)
print(prediction)
