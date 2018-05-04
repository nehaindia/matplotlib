import matplotlib.pyplot as pl
import numpy as np

data = np.loadtxt('fakedata.txt')
# plot the first column as x, and second column as y
pl.plot(data[:,0], data[:,1], 'ro')
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10)
pl.show()
