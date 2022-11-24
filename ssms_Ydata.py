import numpy as np

# ydata from csv file
ydata = np.genfromtxt('Ydata/Y_Cs.csv', delimiter=',')

# generate xdata from 300 to -300
xdata = []
max = 300
x = max
dx = 25
while x >= -max:
    xdata.append(x)
    x -= dx


sxdata = np.array(xdata, dtype=np.float64)
sydata = np.array(ydata, dtype=np.float64)
