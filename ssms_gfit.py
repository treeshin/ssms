import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## which data to use
from ssms_MVdata import xdata
from ssms_mving import ydata


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
print(ydata)
print(xdata)



def func(x, a, b, c, d):
    return a*np.exp(-((np.array(x)-b)**2)/(2*c**2))+d
# [warning] b != 0

plt.plot(xdata, ydata, 'k.', label='data')

popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()

print(popt)
