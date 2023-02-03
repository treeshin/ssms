import glob
import re
import numpy as np
from scipy.interpolate import interp1d
import scipy

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

filenames = glob.glob('MVdata_P1/MV_Cs_0*.csv') #+ glob.glob('MVdata_P1/MV_Ba_3*.csv')
ynew=np.zeros((len(filenames),1000)) # matrix for curves averaging
j=0 # for ynew indexing

for filename in filenames:
    num = [int(s) for s in re.findall(r'\d+', filename)]
    velocity = num[1] # get velocity from filename
    ydata = np.genfromtxt(filename, delimiter=',') # get ydata from csv
    ## Generate xdata and tdata
    xdata = [0] # normalized time scale [0, 8]
    tdata = [0] # raw time scale += 0.1 sec
    [x, t, L] = [0, 0, 7]
    dx = L/(len(ydata)-1)
    # dx = 100000*velocity/36000 # to set dx with velocity
    while len(xdata) < len(ydata):
        x += dx
        xdata.append(x)
        t += 0.1
        tdata.append(t)
    xdata[len(xdata)-1] = L # to avoid truncation error


## MOVING AVERAGE
    arr = ydata
    window_size = 6   
    i = 0
    ## Initialize an empty list to store moving averages
    moving_averages = []
    while i < len(arr):
        if i < window_size:
                window_average = round(np.sum(arr[0:i+1]) / (i+1), 2)
        else:
                window_average = round(np.sum(arr[i-window_size+1:i+1]) / window_size, 2)
        ## Store the average of current
        ## Window in moving average list
        moving_averages.append(window_average)
        ## Shift window to right by one position
        i += 1
    ydata = moving_averages

    ## SAV-GOL FILTER
    # ydata = scipy.signal.savgol_filter(ydata, window_length = 6, polyorder = 3)
    
    ## Averaging the curves    
    f = interp1d(xdata, ydata, kind='linear')
    xnew = np.linspace(0, L, num=1000, endpoint=True) # xnew for average curve
    ynew[j,:] = (f(xnew)) # ynew for average curve
    j+=1 # for ynew indexing

    ## Plotting the curves
    plt.plot(xdata, ydata, 'k-', label=filename, alpha=0.5) # plot each experimental curve

ynew_mean = np.zeros(1000) # matrix for average curve
i=0 # for ynew_mean indexing
while i < len(ynew[0]):
    ynew_mean[i] = np.mean(ynew[:,i]) # derive average of ynew
    i+=1 # for ynew_mean indexing

## PLOT SETTINGS 
 


plt.xlabel('Time(sec)')
plt.ylabel('Counts per second(cps)')
plt.xlim([0,7])
plt.ylim([6000,18000])
# plt.legend()
plt.grid(True, linestyle='--')
plt.tick_params(direction='in')
plt.plot(xnew, ynew_mean, 'r--', linewidth=3)



plt.show()

## Print average curve values
print(*ynew_mean)