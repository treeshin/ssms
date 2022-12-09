# Program to calculate moving average using numpy
  
import numpy as np
from ssms_MVdata import xdata, ydata
  
arr = ydata
window_size = 6
  

i = 0

# Initialize an empty list to store moving averages
moving_averages = []
  
# Loop through the array t o
#consider every window of size 3
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


