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

#"US_WAGE":{
#"file":"USWAGE.csv",
#"size":240,
#"from":1774,
#"to":2013,
#"url":dataurl+"uswage/export.php?year_source=1774&year_result=2013&use[]=UNSKILLED&use[]=MANCOMP"
#},

"UK_RPI":{
"file":"UKRPINAE.csv",
"header":["Year","Retail Price Index (2010 = 100)"],
"size":805,
"title":"The Annual RPI for Britain, 1209 to 2013",
"xlabel":"Year",
"from":1209,
"to":2013,
"ylabel":"CPI",
"url":dataurl+"ukearncpi/export.php?year_source=1209&year_result=2013&use[]=CPI&use[]=NOMINALEARN&use[]=REALEARN"},

"UK_AANE":{
"file":"UKRPINAE.csv",
"header":["Year","Average Annual Nominal Earnings (2010 = 100)"],
"size":805,
"title":"The Average Annual Nominal Earnings for Britain, 1209 to 2013",
"xlabel":"Year",
"from":1209,
"to":2013,
"ylabel":"CPI",
"url":dataurl+"ukearncpi/export.php?year_source=1209&year_result=2013&use[]=CPI&use[]=NOMINALEARN&use[]=REALEARN"},

"UK_AARE":{
"file":"UKRPINAE.csv",
"header":["Year","Average Annual Real Earnings (2010 = 100)"],
"size":805,
"title":"The Average Annual Real Earnings for Britain, 1209 to 2013",
"xlabel":"Year",
"from":1209,
"to":2013,
"ylabel":"CPI",
"url":dataurl+"ukearncpi/export.php?year_source=1209&year_result=2013&use[]=CPI&use[]=NOMINALEARN&use[]=REALEARN"},

}
