""" Test code for existing dataset

Author : Kim Seonghyun <shyeon.kim@scipi.net>
"""

import time
import os
import math
import numpy as np
import pandas as pd

def pick_headers(dataframe, headers, log=False):
    df = dataframe[headers]

    tempvals = []
    for row in df.iterrows():
        tempvals.append([int(row[1][0]),row[1][1]])

    dates = [int(q[0]) for q in tempvals]
    values = [float(str(q[1]).replace(',','')) for q in tempvals]

    if True == log:
        for i,d in enumerate(values):
            if d <= 0.0:
                values[i] = None
            else:
                values[i] = math.log(d)
    return dates, values

def load_dataframe(dataset):
    datafile = "./data/"+dataset["file"]
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

