'''
Questions we want to answer:
   What is the price in the future?
Steps we need to take:
Lable the information [done]
Inspect information and get most important attributes
Drop none significant information

'''''

import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('imports-85.data')
df.dropna(inplace=True)

X = df[['compression_ratio', 'city_mpg', 'peak_rpm']].sort_values('compression_ratio', ascending=True)
X = X.replace('?', 100)
X = np.array(X) 

y = df['price'].replace('?', 100)
y = pd.to_numeric(y)
y = np.array(y)
# X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

# plt.scatter(y, X)
plt.title('Price vs highway mpg')
plt.xlabel('Symboling')
plt.ylabel('Price')
# plt.show()
