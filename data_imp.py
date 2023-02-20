import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
import sklearn

data = pd.read_csv('C:/Users/jojo/OneDrive/Documents/GitHub/proj_final/data.csv')  # load data set
#print(data.head(20))
X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
Z = data.iloc[:, 2].values.reshape(-1, 1)

fig = plt.figure()
ax = plt.axes(projection='3d')


plt.xlabel("Time Exercised Regardless of Acitivity")
plt.ylabel("Calories burned")
plt.clabel("Weight")
plt.title("Time vs Calories vs Weight!")
ax.scatter3D(X, Y, Z, c=Z, cmap='Greens')
ax.plot3D(X, Y, Z, 'gray')
plt.show()
