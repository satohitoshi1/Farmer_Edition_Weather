import datetime
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
yesterday = today + relativedelta(days=-5)

print(yesterday)
