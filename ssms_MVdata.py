import numpy as np

## ydata from csv file
ydata = np.genfromtxt('MVdata/MV_Cs_1_4.csv', delimiter=',')
ndata = np.genfromtxt('MVdata/MV_Non_7_4.csv', delimiter=',')
ydata = ydata - ndata

## generate xdata from 300 to -300
xdata = []
max = 344
x = max

## change dx according to car speed
dx = 14

while len(xdata) < len(ydata):
    xdata.append(x)
    x -= dx

xdata = np.array(xdata, dtype=np.float64)
ydata = np.array(ydata, dtype=np.float64)

