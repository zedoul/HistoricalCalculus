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
    print "real price based on RPI is " + str(price(d1)) + "£"
    print "labour price based on wage is " + str(price(d2)) + "£"
    print "income price based on GDP is " + str(price(d3)) + "£"

def JP_measure(amount, fromyear, toyear):
    d1 = histcalc.JP_CPI_measure(amount, fromyear, toyear)

    print "The price of " + str(amount) + "¥ in " + str(fromyear)
    print ""
    print "In " + str(toyear) + " :"
    def price(x): return '%1.2f'%x
    print "real price based on CPI is " + str(price(d1)) + "¥"

#print "===================================="
#UK_measure(14, 1878, 2013)
print "===================================="
JP_measure(20, 1923, 2011)

