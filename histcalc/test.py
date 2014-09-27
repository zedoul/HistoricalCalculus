# -*- coding: utf-8 -*-

from data import data
from data import datasets

#print datasets.datasets

def UK_RPI_val(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_RPI"]
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    rate = values[-1] / values[index]
    return amount * rate

def UK_labour_val(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_AANE"]
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    rate = values[-1] / values[index]
    return amount * rate

def UK_income_val(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_NominalGDP"]
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    rate = values[-1] / values[index]
    return amount * rate

def result(amount, fromyear, toyear):
    d1 = UK_RPI_val(amount, fromyear, toyear)
    d2 = UK_labour_val(amount, fromyear, toyear)
    d3 = UK_income_val(amount, fromyear, toyear)

    print "The price of GB pound " + str(amount) + "£ in " + str(fromyear)
    print "In " + str(toyear) + " :"
    def price(x): return '$%1.2f'%x
    print "real price based on RPI is " + str(price(d1)) + "£"
    print "labour price based on wage is " + str(price(d2)) + "£"
    print "income price based on GDP is " + str(price(d3)) + "£"

result(1, 1830, 2013)
