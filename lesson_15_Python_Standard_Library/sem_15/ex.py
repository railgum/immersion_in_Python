import calendar

c = calendar.Calendar()
for i in c.itermonthdays2(2023, 10):
    print(i, end=' ')