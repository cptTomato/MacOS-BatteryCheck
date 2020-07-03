
#Modules
import os
from openpyxl import load_workbook
import time
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

#creating the list
meinPlot = []


# processs to capture the data
# creating the csv (database) and catching the data with terminal commands
# writing data ind the csv
# waiting 30 seconds and sending infos, that it is still working
# rewind that until range in for is over

for p in range(0,60):
    akkuMon = str(os.popen("pmset -g batt").read())
    x = akkuMon.split()
    date = str(os.popen("date").read())
    y = date.split()
    cpuMon = str(os.popen("top -l 2 | grep -E \"^CPU\"").read())
    z = cpuMon.split()
    datenbank = open("datenbank.csv","a")
    datenbank.write(x[7] + ";")
    meinPlot.append(x[7])
    datenbank.write(y[3] + ";")
    datenbank.write(z[2] + "\n")
    datenbank.close()
    time.sleep(30)
    print("more Data nomnomnom")
    
# ploting and saving your data
plt.plot(meinPlot)
plt.show()
plt.savefig("AkkuLeistung.png")

# finish line
print("done")
