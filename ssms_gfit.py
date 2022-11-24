import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## which data to use
from ssms_Ydata import sxdata, sydata

from ssms_mving import xdata, ydata

## subtracting background
# ydata = ydata - np.amin(ydata)

## normalizing activity
ydata = ydata*100 / 81.73
sydata = sydata*100 / 81.25

## cutting the tails
result = np.where(ydata == np.amax(ydata))
peak = result[0]
print(ydata)
if peak[0]*2 <= len(ydata):
    ydata = ydata[0:peak[0]*2+1]
    xdata = xdata[0:peak[0]*2+1]
    print(ydata)

else:
    ydata = ydata[2*peak[0]-len(ydata)+1:len(ydata)]
    xdata = xdata[2*peak[0]-len(xdata)+1:len(xdata)]

## adjust xdata that x=0 at ydata peak
i = 1
dx = 14
while peak[0] + i <= len(ydata) - 1 or peak[0] - i >= 0:
    xdata[peak[0]] = 0
    xdata[peak[0]+i] =  16 * i
    xdata[peak[0]-i] = -16 * i
    i += 1


def func(x, A, x0, c, d):
    return A*np.exp(-((np.array(x)-x0)**2)/(2*c**2))+d
# [warning] b != 0

plt.plot(xdata, ydata, 'k--', lw=5, alpha=0.8, label='data')
# plt.plot(sxdata, sydata, 'r.', label='data')


popt, pcov = curve_fit(func, sxdata, sydata, bounds=[[0,-50,-np.inf,-np.inf],[8000,50,np.inf,5000]])

plt.plot(xdata, func(xdata, *popt), 'r-', lw=10, alpha=0.6,
         label='fit: A=%5.3f, x0=%5.3f, c=%5.3f, d=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


plt.show()

# print(popt)
