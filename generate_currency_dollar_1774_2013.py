# -*- coding: utf-8 -*-
from __future__ import print_function
from histcalc import histcalc
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

def US_measure(amount, fromyear, toyear):
    d1 = histcalc.US_CPI_measure(amount, fromyear, toyear)
    ret = ""
    ret += "The price of "+str(amount)+"$ in "+str(fromyear)+"\n"
    ret += "==============================\n"
    if d1:
        def price(x): return locale.format('%1.2f',x,grouping=True)
        ret += "- Real price based on CPI is " + str(price(d1)) + "$, 한화 " +str(price(1061.38*d1)) +"₩\n"
    else :
        ret += "- Not recorded\n"
    return ret

def generate_markdown(from_year,to_year,curr_year):
    ret = "미국 달러 (United States Dollar)\n"
    ret += "==================================\n"
    ret += "- 환율 1달러 당 1061.38원 적용 (2014년 10월 3일)\n"
    ret += "\n"
    for year in range(from_year,to_year+1):
        ret += US_measure(1, year, curr_year) 
        ret += "\n"
    return ret;

source = 'docs/currency/USDOLLAR_1774_2013.md'
f = open(source,'w')
txt = generate_markdown(1774,2013,2013)
print(txt, file=f)
f.close()
