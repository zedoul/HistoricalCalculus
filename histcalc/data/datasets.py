dataurl = "http://www.measuringworth.com/datasets/"

datasets = {
"US_CPI":{
"file":"USCPI.csv",
"header":["Year","U.S. Consumer Price Index *"],
"size":240,
"title":"The Annual Consumer Price Index for the United States, 1774-2013",
"xlabel":"Year",
"from":1774,
"to":2013,
"ylabel":"CPI",
"url":dataurl+"uscpi/export.php?year_source=1774&year_result=2013"},

"UK_GOLD_OFFICAL":{
"file":"UKGOLDOFF.csv",
"header":["Year","British Official Price (British pounds per fine ounce end of year)"],
"size":689,
"title":"British Official Price 1257-1945 (British pounds per fine ounce end of year)",
"xlabel":"Year",
"from":1257,
"to":1945,
"ylabel":"Price",
"url":dataurl+"gold/export.php?year_source=1257&year_result=1945&British=on&us=&newyork=&goldsilver=&london="},

#"US_WAGE":{
#"file":"USWAGE.csv",
#"size":240,
#"from":1774,
#"to":2013,
#"url":dataurl+"uswage/export.php?year_source=1774&year_result=2013&use[]=UNSKILLED&use[]=MANCOMP"
#},

# GDP
"UK_NGDP":{
"file":"UKGDP.csv",
"header":["Year","Nominal GDP (million of pounds)"],
"size":184,
"title":"Nominal GDP for Britain, 1830 to 2013",
"xlabel":"Year",
"from":1830,
"to":2013,
"ylabel":"Nominal GDP (millions of pounds)",
"url":dataurl+"ukgdp/export.php?year_source=1830&year_result=2013&use[]=GDPC&use[]=GDPK&use[]=DEFIND&use[]=POP&use[]=GDPCP&use[]=GDPKP"},

"UK_RGDP":{
"file":"UKGDP.csv",
"header":["Year","Real GDP (millions of 2008 pounds)"],
"size":184,
"title":"Real GDP for Britain, 1830 to 2013",
"xlabel":"Year",
"from":1830,
"to":2013,
"ylabel":"Real GDP (millions of 2008 pounds)",
"url":dataurl+"ukgdp/export.php?year_source=1830&year_result=2013&use[]=GDPC&use[]=GDPK&use[]=DEFIND&use[]=POP&use[]=GDPCP&use[]=GDPKP"},

"UK_GDPDef":{
"file":"UKGDP.csv",
"header":["Year","GDP Deflator (index 2008 = 100)"],
"size":184,
"title":"GDP Deflator for Britain, 1830 to 2013",
"xlabel":"Year",
"from":1830,
"to":2013,
"ylabel":"GDP Deflator(index 2008 = 100)",
"url":dataurl+"ukgdp/export.php?year_source=1830&year_result=2013&use[]=GDPC&use[]=GDPK&use[]=DEFIND&use[]=POP&use[]=GDPCP&use[]=GDPKP"},

"UK_Population":{
"file":"UKGDP.csv",
"header":["Year","Population (in thousands)"],
"size":184,
"title":"Population for Britain, 1830 to 2013",
"xlabel":"Year",
"from":1830,
"to":2013,
"ylabel":"Population(in thousands)",
"url":dataurl+"ukgdp/export.php?year_source=1830&year_result=2013&use[]=GDPC&use[]=GDPK&use[]=DEFIND&use[]=POP&use[]=GDPCP&use[]=GDPKP"},

"UK_GDPCapita":{
"file":"UKGDP.csv",
"header":["Year","Nominal GDP per capita (current pounds)"],
"size":184,
"title":"Nominal GDP per capita for Britain, 1830 to 2013",
"xlabel":"Year",
"from":1830,
"to":2013,
"ylabel":"Nominal GDP per capita(current pounds)",
"url":dataurl+"ukgdp/export.php?year_source=1830&year_result=2013&use[]=GDPC&use[]=GDPK&use[]=DEFIND&use[]=POP&use[]=GDPCP&use[]=GDPKP"},

"UK_RealGDP":{
"file":"UKGDP.csv",
"header":["Year","Real GDP per capita (2008 pounds)"],
"size":184,
"title":"Real GDP per capita for Britain, 1830 to 2013",
"xlabel":"Year",
"from":1830,
"to":2013,
"ylabel":"Real GDP per capita(2008 pounds)",
"url":dataurl+"ukgdp/export.php?year_source=1830&year_result=2013&use[]=GDPC&use[]=GDPK&use[]=DEFIND&use[]=POP&use[]=GDPCP&use[]=GDPKP"},

# RPI
"UK_RPI":{
"file":"UKRPINAE.csv",
"header":["Year","Retail Price Index (2010 = 100)"],
"size":805,
"title":"The Annual RPI for Britain, 1209 to 2013",
"xlabel":"Year",
"from":1209,
"to":2013,
"ylabel":"Retail Price Index (2010 = 100)",
"url":dataurl+"ukearncpi/export.php?year_source=1209&year_result=2013&use[]=CPI&use[]=NOMINALEARN&use[]=REALEARN"},

"UK_AANE":{
"file":"UKRPINAE.csv",
"header":["Year","Average Annual Nominal Earnings (2010 = 100)"],
"size":805,
"title":"The Average Annual Nominal Earnings for Britain, 1209 to 2013",
"xlabel":"Year",
"from":1209,
"to":2013,
"ylabel":"Average Annual Nominal Earnings (2010 = 100)",
"url":dataurl+"ukearncpi/export.php?year_source=1209&year_result=2013&use[]=CPI&use[]=NOMINALEARN&use[]=REALEARN"},

"UK_AARE":{
"file":"UKRPINAE.csv",
"header":["Year","Average Annual Real Earnings (2010 = 100)"],
"size":805,
"title":"The Average Annual Real Earnings for Britain, 1209 to 2013",
"xlabel":"Year",
"from":1209,
"to":2013,
"ylabel":"Average Annual Real Earnings (2010 = 100)",
"url":dataurl+"ukearncpi/export.php?year_source=1209&year_result=2013&use[]=CPI&use[]=NOMINALEARN&use[]=REALEARN"},

# Japan
"JP_CPI":{
"file":"JPGDP.csv",
"header":["Year","Consumer Price Index (index year 2000 = 100,000)"],
"size":133,
"title":"Consumer Price Index for Japan, 1879 to 2011",
"xlabel":"Year",
"from":1879,
"to":2011,
"ylabel":"Consumer Price Index (index year 2000 = 100,000)",
"url":dataurl+"japandata/export.php?year_source=1879&year_result=2011&use[]=NOMGDP&use[]=REALGDP&use[]=DEFLATOR&use[]=GDPPC&use[]=RGDPPC&use[]=POPULATION&use[]=CPI&use[]=AVEWAGE"},

"JP_NGDP":{
"file":"JPGDP.csv",
"header":["Year","Nominal GDP (billions of yen)"],
"size":133,
"title":"Nominal GDP (billions of yen) of Japan, 1879 to 2011",
"xlabel":"Year",
"from":1879,
"to":2011,
"ylabel":"Nominal GDP (billions of yen)",
"url":dataurl+"japandata/export.php?year_source=1879&year_result=2011&use[]=NOMGDP&use[]=REALGDP&use[]=DEFLATOR&use[]=GDPPC&use[]=RGDPPC&use[]=POPULATION&use[]=CPI&use[]=AVEWAGE"},

"JP_GDPCapita":{
"file":"JPGDP.csv",
"header":["Year","Nominal GDP per Capita (thousands of yen)"],
"size":133,
"title":"Nominal GDP per Capita (thousands of yen) of Japan, 1879 to 2011",
"xlabel":"Year",
"from":1879,
"to":2011,
"ylabel":"Nominal GDP per Capita (thousands of yen)",
"url":dataurl+"japandata/export.php?year_source=1879&year_result=2011&use[]=NOMGDP&use[]=REALGDP&use[]=DEFLATOR&use[]=GDPPC&use[]=RGDPPC&use[]=POPULATION&use[]=CPI&use[]=AVEWAGE"},

}
