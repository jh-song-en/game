from datetime import date

date1 = date(1901, 1, 1)
date2 = date(2000, 12, 31)
dates = date2 - date1
print((dates.days) // 7)
