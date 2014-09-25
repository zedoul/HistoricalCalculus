""" Test code for existing dataset

Author : Kim Seonghyun <shyeon.kim@scipi.net>
"""

import time
import os
import math
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
from matplotlib import gridspec

dataurl = "http://www.measuringworth.com/datasets/"
datasets = {
"USCPI":{"file":"USCPI.csv","size":240,"url":dataurl+"uscpi/export.php?year_source=1774&year_result=2013"},
"USWAGE":{"file":"USWAGE.csv","size":240,"url":dataurl+"uswage/export.php?year_source=1774&year_result=2013&use[]=UNSKILLED&use[]=MANCOMP"},
}

def load_dataframe(dataset):
    datafile = dataset["file"]
    assert(os.path.isfile(datafile))
    datasize = dataset["size"]
    df = pd.read_csv(datafile, nrows=datasize)
    df.iloc[0]
    return df

if __name__ == '__main__':
    import sys
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0):
        print ("Requires Python 2.7.x")
        exit()
    del sys

    dataset = datasets["USCPI"]
    df = load_dataframe(dataset)

    quotes = []
    for row in df.iterrows():
        quotes.append([int(row[1][0]),row[1][1]])

    if len(quotes) == 0:
        raise SystemExit

    dates = [q[0] for q in quotes]
    opens = [q[1] for q in quotes]

    fig, ax = plt.subplots()
    ax.plot(dates, opens, '-')

    # format the ticks
    ax.autoscale_view()

    # format the coords message box
    def price(x): return '$%1.2f'%x
    ax.fmt_xdata = DateFormatter('%Y')
    ax.fmt_ydata = price
    ax.grid(True)
    plt.xlim(1777,2015)
    fig.autofmt_xdate()

    plt.title('The Annual Consumer Price Index for the United States, 1774-2013') 
    plt.xlabel('Year')
    plt.ylabel('CPI')
    fig.savefig("USCPI.png")

