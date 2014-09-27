import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
from matplotlib import gridspec

import data
from datasets import datasets

def generate_plots(key, dataset):
    df = data.load_dataframe(dataset)
    df = df[dataset["header"]]
    quotes = []
    for row in df.iterrows():
        quotes.append([int(row[1][0]),row[1][1]])
    
    if len(quotes) == 0:
        raise SystemExit
    
    dates = [int(q[0]) for q in quotes]
    opens = [float(str(q[1]).replace(',','')) for q in quotes]
    
    fig, ax = plt.subplots()
    ax.plot(dates, opens, '-')
    
    # format the ticks
    ax.autoscale_view()
    
    # format the coords message box
    def price(x): return '$%1.2f'%x
    ax.fmt_xdata = DateFormatter('%Y')
    ax.fmt_ydata = price
    ax.grid(True)
    plt.xlim(dataset["from"],dataset["to"])
    fig.autofmt_xdate()

    plt.title(dataset['title']) 
    plt.xlabel(dataset['xlabel'])
    plt.ylabel(dataset['ylabel'])
    fig.savefig("plot_"+key+".png")

if __name__ == '__main__':
    import sys
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0):
        print ("Requires Python 2.7.x")
        exit()
    del sys

    for key, dataset in datasets.iteritems():
        generate_plots(key,dataset)
