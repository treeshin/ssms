## python script to clear csv files
import numpy as np
import openpyxl
import glob
import csv
inputnames = glob.glob('*/test/20230208_*.xlsx')
k = 1
for inputname in inputnames:
    print(inputname)
    wb = openpyxl.load_workbook(inputname)
    sh = wb.active # automatically selects Sheet1?
    i = 69
    j = 4
    SE1 = []
    SE2 = []
    velocity = sh.cell(row=6, column=3).value
    velocity = int(velocity.split()[0])
    print(velocity)
    while sh.cell(row=i, column=j).value != None:
        LE1 = sh.cell(row=i, column=j).value
        HE1 = sh.cell(row=i, column=j+1).value
        SE1.append((LE1 + HE1) * 10)
        LE2 = sh.cell(row=i, column=j+2).value
        HE2 = sh.cell(row=i, column=j+3).value
        SE2.append((LE2 + HE2) * 10)
        i+=1
    print(SE1)
    print(SE2)

    ## Print average curve values
    ## saved at current working directory
    outputname = 'MV_Non_1' + str(k).zfill(2) + '_' + str(velocity) + '.csv'
    with open(outputname,'w+') as f:
        writer = csv.writer(f)
        csv.writer(f, delimiter='\n').writerow(SE1)
        k+=1