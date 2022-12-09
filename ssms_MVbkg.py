import numpy as np
import matplotlib.pyplot as plt

## which data to use
from ssms_mving import xdata, ydata

## cutting the tails
result = np.where(ydata == np.amin(ydata))
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
dx = 8.33
while peak[0] + i <= len(ydata) - 1 or peak[0] - i >= 0:
    xdata[peak[0]] = 0
    xdata[peak[0]+i] =  dx * i
    xdata[peak[0]-i] = -dx * i
    i += 1



plt.plot(xdata, ydata, 'k-', lw=5, alpha=0.8, label='data')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


plt.show()

# print(popt)
