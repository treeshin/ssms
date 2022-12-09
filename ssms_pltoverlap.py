import glob
import re
import numpy as np
import matplotlib.pyplot as plt


filenames = glob.glob('MVdata/MV_Cs_*.csv') ## + glob.glob('MVdata/MV_Cs_5*.csv')

for filename in filenames:
    num = [int(s) for s in re.findall(r'\d+', filename)]
    velocity = num[1]

    # ydata from csv file
    ydata = np.genfromtxt(filename, delimiter=',')

    ## generate xdata from 300 to -300
    xdata = []
    max = 344
    x = max

    ## change dx according to car speed
    dx = 100000*velocity/36000

    while len(xdata) < len(ydata):
        xdata.append(x)
        x -= dx

    xdata = np.array(xdata, dtype=np.float64)
    ydata = np.array(ydata, dtype=np.float64)


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

    xdata = np.array(xdata, dtype=np.float64)
    ydata = np.array(ydata, dtype=np.float64)

    ## cutting the tails
    result = np.where(ydata == np.amax(ydata))
    peak = result[0]
    if peak[0]*2 <= len(ydata):
        ydata = ydata[0:peak[0]*2+1]
        xdata = xdata[0:peak[0]*2+1]

    else:
        ydata = ydata[2*peak[0]-len(ydata)+1:len(ydata)]
        xdata = xdata[2*peak[0]-len(xdata)+1:len(xdata)]

    ## adjust xdata that x=0 at ydata peak
    i = 1
    while peak[0] + i <= len(ydata) - 1 and peak[0] - i >= 0:
        xdata[peak[0]] = 0
        ## points before the peak
        xdata[peak[0]-i] =  dx * i

        ## points after the peak
        xdata[peak[0]+i] = -dx * i
        i += 1

    # ydata = ydata - np.amin(ydata)
    
    if velocity < 9:
        plt.plot(xdata, ydata, 'r.', lw=5, alpha=0.3, label=filename)
    elif 9 <= velocity < 18:
        plt.plot(xdata, ydata, 'g.', lw=5, alpha=0.3, label=filename)
    else:
        plt.plot(xdata, ydata, 'b.', lw=5, alpha=0.3, label=filename)




plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-1000,1000])
plt.ylim([6000,15000])
plt.legend()
plt.grid(True)

plt.show()



