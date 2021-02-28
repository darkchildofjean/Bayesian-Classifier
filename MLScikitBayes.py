#I got this to work all the way up to the calculation of the accuracy_score
#A prediction from this says that I do not play Tennis on the given day.

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import math

le = preprocessing.LabelEncoder()

outlook = ['Sunny','Sunny', 'Overcast', 'Rain','Rain','Rain', 'Overcast','Sunny','Sunny','Rain', 'Sunny','Overcast','Overcast', 'Rain']
temp = ['Hot','Hot','Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool','Mild','Mild','Mild','Hot', 'Mild']
humidity = ['High','High','High','High', 'Normal','Normal','Normal', 'High', 'Normal','Normal','Normal','High','Normal','High']
wind = ['Weak','Strong', 'Weak','Weak','Weak','Strong', 'Strong','Weak','Weak','Weak','Strong','Strong', 'Weak','Strong']
play = ['No','No','Yes','Yes','Yes', 'No', 'Yes','No', 'Yes','Yes','Yes','Yes', 'Yes', 'No']

outlook_encoded=le.fit_transform(outlook)
temp_encoded=le.fit_transform(temp)
humidity_encoded=le.fit_transform(humidity)
wind_encoded=le.fit_transform(wind)
play_encoded=le.fit_transform(play)
print(outlook_encoded)
print(temp_encoded)
print(humidity_encoded)
print(wind_encoded)
print(play_encoded)

features = list(zip(outlook_encoded, temp_encoded, humidity_encoded, wind_encoded))

tennis = GaussianNB()

tennis.fit(features, play_encoded)

#In this prediction the outcome of 0 = I won't play tennis on
#that day...While an outcome of 1 = I will play Tennis
#This one should come back as 0, which it does.
predicted = tennis.predict([[2,0,0,0]])
print(predicted)

X_train, X_test, y_train, y_test = train_test_split(features, play_encoded, test_size=0.3)
tests = tennis.predict(X_test)
accuracy_score(tests, y_test)
