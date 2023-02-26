
import matplotlib.pyplot as plt
import csv
import numpy as np
x = []
y = []
  
with open('C:/Users/jojo/OneDrive/Documents/GitHub/proj_final/data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))

X = np.linspace(0, 100, 100)
m = (float(y[len(y)-3]) - float(y[2]))/(float(x[len(x)-3]) - float(x[2])) #predict slope of graph
b = int(y[len(y)-3]) - (int(m)*int(x[len(x)-3]))
Y = m*X + b
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(X,Y, color = 'b', marker = 'o',label = "Trend")

plt.xticks(rotation = 25)
plt.xlabel('Time')
plt.ylabel('Calories burned')
plt.title('Exercise Graph', fontsize = 20)
plt.grid()
plt.legend()
plt.show()