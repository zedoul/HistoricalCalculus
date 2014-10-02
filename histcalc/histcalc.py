from data import data
from data import datasets

def get_rate(amount, values, index):
    if 0 == values[index]:
        return None
    rate = values[-1] / values[index]
    return amount * rate

def UK_RPI_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_RPI"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    _, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    return get_rate(amount, values, index)

def UK_EarningIndex_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_AANE"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    _, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    return get_rate(amount, values, index)

def UK_GDPperCapita_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["UK_GDPCapita"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    _, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    return get_rate(amount, values, index)

def JP_CPI_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["JP_CPI"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    _, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    return get_rate(amount, values, index)

def JP_GDPperCapita_measure(amount, fromyear, toyear=2013):
    dataset = datasets.datasets["JP_GDPCapita"]
    assert (fromyear >= dataset["from"])
    assert (toyear <= dataset["to"])
    df = data.load_dataframe(dataset)
    _, values = data.pick_headers(df,dataset["header"])
    index = fromyear - dataset["from"]
    return get_rate(amount, values, index)
