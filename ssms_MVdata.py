import numpy as np
import re

filename = 'MVdata/MV_Non_01_3.csv'
num = [int(s) for s in re.findall(r'\d+', filename)]
velocity = num[1]

# ydata from csv file
ydata = np.genfromtxt(filename, delimiter=',')

# ## subtract nondata from ydata
# ndata = np.genfromtxt('MVdata/MV_Non_7_4.csv', delimiter=',')
# ydata = ydata - ndata

## generate xdata from 300 to -300
xdata = []
max = 344
x = max

## change dx according to car speed
dx = 100000*velocity/36000
print(dx)

while len(xdata) < len(ydata):
    xdata.append(x)
    x -= dx

xdata = np.array(xdata, dtype=np.float64)
ydata = np.array(ydata, dtype=np.float64)
