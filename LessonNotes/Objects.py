'''                 Using Objects


'''
#  from datetime import datetime
#  datetime(2030, 1, 1)
# datetime.datetime(2030, 1, 1, 0, 0)
#  datetime(2959, 5, 1, 12)
# datetime.datetime(2959, 5, 1, 12, 0)
#  datetime(2030, 4, 1) - datetime(2030, 1, 1)
# datetime.timedelta(days=90)

# datetime.now()
# datetime.datetime(2021, 1, 21, 0, 31, 50, 601619)

# datetime(2030, 1, 1) - datetime.now()
# datetime.timedelta(days=3266, seconds=84341, microseconds=792847)
#  now = datetime(2030, 1, 1) - datetime.now()
#  diff.days
# 3266
#  now = datetime.now()
#  now.year
# 2021
#  now.day
# 21



from datetime import datetime
now = datetime.now()
bday = datetime(now.year, 2, 1)
if bday < now:
	bday = datetime(now.year + 1, 2, 1)
diff = bday - now
print(diff.days)  # 11
