""" Test code for existing dataset

Author : Kim Seonghyun <shyeon.kim@scipi.net>
"""

import time
import os
import math
import numpy as np
import pandas as pd

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

