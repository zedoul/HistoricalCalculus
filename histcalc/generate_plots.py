import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
from matplotlib import gridspec

import math
from data import data
from data.datasets import datasets

def generate_plots(key, dataset, log=False):
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df, dataset["header"], log)
    
    fig, ax = plt.subplots()
    ax.plot(dates, values, '-')
    
    # format the ticks
    ax.autoscale_view()
    
    # format the coords message box
    def price(x): return '%1.2f'%x
    ax.fmt_xdata = DateFormatter('%Y')
    ax.fmt_ydata = price
    ax.grid(True)
    plt.xlim(dataset["from"],dataset["to"])
    fig.autofmt_xdate()

    plt.title(dataset['title']) 
    plt.xlabel(dataset['xlabel'])

    if True == log:
        plt.ylabel(dataset['ylabel'] + " logscale")
        fig.savefig("./plots/plot_"+key+"_log.png")
    else :
        plt.ylabel(dataset['ylabel'])
        fig.savefig("./plots/plot_"+key+".png")
    plt.close()

if __name__ == '__main__':
    import sys
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0):
        print ("Requires Python 2.7.x")
        exit()
    del sys

    for key, dataset in datasets.iteritems():
        generate_plots(key,dataset)
        generate_plots(key,dataset,True)
