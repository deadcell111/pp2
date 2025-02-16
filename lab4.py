import datetime
x = datetime.datetime.now()
five_days_ago = datetime.datetime(x.year,x.month,x.day - 5)
today = datetime

yesterday = datetime.datetime(x.year,x.month,x.day - 1)
tomorrow = datetime.datetime(x.year,x.month,x.day + 1)
micro_second = x.strftime("%f")
def diff(a,b):
    return (a - b).total_seconds()