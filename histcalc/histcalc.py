from data import data
from data import datasets

def UK_RPI_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_RPI"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    rate = values[-1] / values[index]
    return amount * rate

def UK_EarningIndex_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_AANE"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    rate = values[-1] / values[index]
    return amount * rate

def UK_GDPperCapita_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_NominalGDP"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    dates, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    rate = values[-1] / values[index]
    return amount * rate

