import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.interpolate import interp1d

filenames = glob.glob('MVdata_P2_cut/SENSOR_ON/Co_3*.csv')

for filename in filenames:
    ## ydata from csv file
    cutdata = np.genfromtxt(filename, delimiter=',')

cutdata = cutdata.astype(int)
print(cutdata)

filenames = glob.glob('MVdata_P2_cut/MV_Co_3*.csv')
i=0
for filename in filenames:
    ydata = np.genfromtxt(filename, delimiter=',')
    print(cutdata[i][3])
    ydata = (ydata[cutdata[i][0]-1:cutdata[i][3]-1])
    print(ydata)
    np.savetxt(filename, ydata, delimiter=',')
    i+=1