# -*- coding: utf-8 -*-

from histcalc import histcalc

def result(amount, fromyear, toyear):
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

result(1, 1830, 2013)
