# -*- coding: utf-8 -*-
from __future__ import print_function
from histcalc import histcalc
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

def UK_measure(amount, fromyear, toyear):
    d1 = histcalc.UK_RPI_measure(amount, fromyear, toyear)
    ret = ""
    ret += "The price of "+str(amount)+"£ in "+str(fromyear)+"\n"
    ret += "==============================\n"
    if d1:
        def price(x): return locale.format('%1.2f',x,grouping=True)
        ret += "- Real price based on RPI is " + str(price(d1)) + "£, 한화 " +str(price(1696.96*d1)) +"₩\n"
    else :
        ret += "- Not recorded\n"
    return ret

def generate_markdown(from_year,to_year,curr_year):
    ret = "파운드 스털링 (Pound sterling)\n"
    ret += "==================================\n"
    ret += "- 1960년 이전 : 1파운드 = 20실링, 1실링 = 12펜스\n"
    ret += "- 1960년 이후 : 1파운드 = 100펜스\n"
    ret += "- 환율 1파운드 당 1696.96원 적용 (2014년 9월 28일)\n"
    ret += "\n"
    for year in range(from_year,to_year+1):
        ret += UK_measure(1, year, curr_year) 
        ret += "\n"
    return ret;

source = 'docs/currency/POUNDSTERLING_1209_1829.md'
f = open(source,'w')
txt = generate_markdown(1209,1829,2013)
print(txt, file=f)
f.close()
