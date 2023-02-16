## python script to clear csv files
import glob
filenames = glob.glob('*/test/MV_Non_*.csv')
for filename in filenames:
    print(filename)
    ## opening the file with w+ mode truncates the file
    ## [CAUTION] check before doing it
    f = open(filename, "w+")
    f.close()