import numpy as np
import matplotlib.pyplot as plt

data = {'Weight-lifting':90,'Aerobics':165,'Skiing':285,'Rowing':210}

x = list(data.keys())
y = list(data.values())

fig = plt.figure(figsize = (10,5))

plt.bar(x,y, color = 'pink', width = 0.5)

plt.xlabel("Activities")
plt.ylabel("Calories burned")
plt.title("Activities vs Calories Burned!")
plt.show()
