import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.interpolate import interp1d

filenames = glob.glob('MVdata/MV_Ba_0*.csv') #+ glob.glob('MVdata/MV_Ba_3*.csv') # number of data = 71
xs=[]
ys=[]
j=0
ynew=np.zeros((len(filenames),1000))

for filename in filenames:
    num = [int(s) for s in re.findall(r'\d+', filename)]
    velocity = num[1]

    ## ydata from csv file
    ydata = np.genfromtxt(filename, delimiter=',')

    # ## deadtime compensation
    # deadtime = 14.31 # Ba-133
    # ydata = np.array(ydata)
    # ydata = ydata/(1-(ydata*deadtime*10**-6))


    ## generate xdata and tdata
    xdata = [0]
    tdata = [0]
    t=0
    L = 8
    x = 0
    # dx = 100000*velocity/36000 # set dx according to car speed
    dx = L/(len(ydata)-1)
    while len(xdata) < len(ydata):
        x += dx
        xdata.append(x)
        t += 0.1
        tdata.append(t)
    xdata[len(xdata)-1] = 8


    

## mving average

    arr = ydata
    window_size = 6   

    i = 0

    # Initialize an empty list to store moving averages
    moving_averages = []
    
    while i < len(arr):
        if i < window_size:
                window_average = round(np.sum(arr[0:i+1]) / (i+1), 2)
        else:
                window_average = round(np.sum(arr[i-window_size+1:i+1]) / window_size, 2)
        
        # Store the average of current
        # window in moving average list
        moving_averages.append(window_average)
        
        # Shift window to right by one position
        i += 1
    
    ydata = moving_averages

    # xdata = np.array(xdata, dtype=np.float64)
    # ydata = np.array(ydata, dtype=np.float64)
    xs+=xdata
    ys+=ydata

    ydata = scipy.signal.savgol_filter(ydata, window_length = 6, polyorder = 3)
    
    f = interp1d(xdata, ydata, kind='linear')
    xnew = np.linspace(0, 8, num=1000, endpoint=True)
    ynew[j,:] = (f(xnew))
    j+=1
    plt.plot(xdata, ydata, 'k-', label=filename)

ynew_mean = np.zeros(1000)
i=0
while i < len(ynew[0]):
    ynew_mean[i] = np.mean(ynew[:,i])
    i+=1



plt.xlabel('time(sec)')
plt.ylabel('true count per second(cps)')
plt.xlim([0,8])
plt.ylim([6000,20000])
# plt.legend()
plt.grid(True)

plt.plot(xnew, ynew_mean, 'r')
plt.show()

print(*ynew_mean)