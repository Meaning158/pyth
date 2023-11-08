import numpy as np
import matplotlib.pyplot as plot
t = np.arange(0, np.pi * 2, 0.1);
a = np.log(t) + np.cos(t)
plot.plot(t, a)
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()