import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import skewnorm

## which data to use
from ssms_mving import xdata, ydata
# from ssms_mving import ydata


## cutting the tails
result = np.where(ydata == np.amax(ydata))
peak = result[0]
print(len(ydata))
print(peak)
print(ydata)
print(xdata)
if peak[0]*2 <= len(ydata):
    ydata = ydata[0:peak[0]*2]
    xdata = xdata[0:peak[0]*2]
else:
    ydata = ydata[2*peak[0]-len(ydata)+1:len(ydata)-1]
    xdata = xdata[2*peak[0]-len(xdata)+1:len(xdata)-1]
# print(ydata)
# print(xdata)

fig, ax = plt.subplots(1, 1)

a = 4
mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')

x = np.linspace(skewnorm.ppf(0.01, a),
                skewnorm.ppf(0.99, a), 100)
ax.plot(x, skewnorm.pdf(x, a),
       'r-', lw=5, alpha=0.6, label='skewnorm pdf')

rv = skewnorm(a)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

vals = skewnorm.ppf([0.001, 0.5, 0.999], a)
np.allclose([0.001, 0.5, 0.999], skewnorm.cdf(vals, a))

r = skewnorm.rvs(a, size=1000)

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()