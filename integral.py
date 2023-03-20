from function import func
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
m = 17.633333333333333
B= -356



a, b = 50,  80 # integral limits
x = np.linspace(20, 100)
y = func(x,m,B)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)

# Make the shaded region
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')
plt.xlabel('Time')
plt.ylabel('Calories burned')
ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=[a, b])
ax.set_yticks([])
plt.title('Exercise Graph ' + "y = " + str(m) + "x + " + str(B), fontsize = 10)
plt.show()