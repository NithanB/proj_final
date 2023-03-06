
import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.patches import Polygon
x = []
y = []
  
with open('C:/Users/jojo/OneDrive/Documents/GitHub/proj_final/data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))

#create linear regression formula

X = np.linspace(20, 100, 100)
m = (float(y[len(y)-3]) - float(y[2]))/(float(x[len(x)-3]) - float(x[2])) #predict slope of graph with manual calculation
b = int(y[len(y)-3]) - (int(m)*int(x[len(x)-3]))
Y = m*X + b


fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(X,Y, color = 'b', marker = 'o',label = "Trend")

plt.xticks(rotation = 25)
plt.xlabel('Time')
plt.ylabel('Calories burned')
plt.title('Exercise Graph ' + "y = " + str(m) + "x + " + str(b), fontsize = 20)

print(m)
print(b)
plt.grid()
plt.legend()
plt.show()