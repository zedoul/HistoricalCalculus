# -*- coding: utf-8 -*-

from histcalc import histcalc

def UK_measure(amount, fromyear, toyear):
    d1 = histcalc.UK_RPI_measure(amount, fromyear, toyear)
    d2 = histcalc.UK_EarningIndex_measure(amount, fromyear, toyear)
    d3 = histcalc.UK_GDPperCapita_measure(amount, fromyear, toyear)

    print "The price of " + str(amount) + "£ in " + str(fromyear)
    print ""
    print "In " + str(toyear) + " :"
    def price(x): return '%1.2f'%x
    print "real price based on RPI is " + str(price(d1)) + "£, 한화 " +str(price(1696.96*d1)) +"₩"
    print "labour price based on wage is " + str(price(d2)) + "£, 한화 " +str(price(1696.96*d2)) +"₩"
    print "income price based on GDP is " + str(price(d3)) + "£, 한화 " +str(price(1696.96*d3)) +"₩"

def JP_measure(amount, fromyear, toyear):
    d1 = histcalc.JP_CPI_measure(amount, fromyear, toyear)

    print "The price of " + str(amount) + "¥ in " + str(fromyear)
    print ""
    print "In " + str(toyear) + " :"
    def price(x): return '%1.2f'%x
    print "real price based on CPI is " + str(price(d1)) + "¥, 한화 "+str(price(9.56*d1))+"₩"

for i in range(1830, 2001):
    print "-------------------------------"
    UK_measure(1, i, 2013)
for i in range(1879, 2001):
    print "-------------------------------"
    JP_measure(1, i, 2011)

