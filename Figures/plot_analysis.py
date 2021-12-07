#!/usr/bin/python
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.patches import Arrow

rc('text', usetex=True)

def func(x):
    return np.sin(2*np.pi*x/10)+1.0/10.0*np.sin(2*np.pi*x)+np.sin(2*np.pi*(x-1.0/4.0))*np.exp(-x/12.0)


x = np.arange(0, 50, 0.01)
y = func(x)

fig, ax = plt.subplots(figsize=(10,5))
plt.tight_layout()
plt.plot(x, y, 'r', linewidth=2)
plt.xlabel('t',size=24)
plt.ylabel('P(t)',size=24)
plt.xticks([])
plt.yticks([])
plt.ylim(-2.4,2.4)

a=0
b=30

# Make the shaded region
ix = np.arange(a, b, 0.01)
iy = func(ix)
verts = [(a, -2.65)] + list(zip(ix, iy)) + [(b, -2.65)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

a=33
b=42
# Make the shaded region
ix = np.arange(a, b, 0.01)
iy = func(ix)
verts = [(a, 1.3)] + list(zip(ix, iy)) + [(b, 1.3)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Make the arrow

a=30
b=50

for idx in range(3,13):
    ix = a+idx #np.arange(a, b, 0.1)
    iy = func(ix)-0.5
    plt.arrow(ix,-2.2,0,iy+2.0,1.1,head_width=0.5, head_length=0.1)
#ax.add_patch(arrows)

plt.text(10, -2.3, r'Convergence: $\displaystyle t \gg \frac{1}{\gamma_{deph}}$', fontsize=20)
plt.text(34, 1.45, r'Sampling: $\displaystyle T_L = \frac{2 \pi}{\omega_L}$', fontsize=20)

plt.subplots_adjust(bottom=0.15)
plt.savefig('Pt_analysis.eps', format='eps')

plt.show()
