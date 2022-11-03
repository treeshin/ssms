import numpy as np

# ydata from csv file
ydata = np.genfromtxt('MV_Cs_2_5.csv', delimiter=',')

# generate xdata from 300 to -300
xdata = []
max = 344
x = max
dx = 14
while len(xdata) < len(ydata):
    xdata.append(x)
    x -= dx

