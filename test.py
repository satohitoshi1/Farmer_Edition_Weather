from datetime import datetime
from dateutil.relativedelta import relativedelta

heading = input("出穂日を入れてください(例2022,8,1)")

dt1 = datetime.strptime(heading, "%Y,%m,%d")
dt2 = datetime.today()

dt3 = dt2 - dt1
print(dt3.days)
