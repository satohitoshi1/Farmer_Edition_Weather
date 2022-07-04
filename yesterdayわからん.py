import os
import datetime
from dateutil.relativedelta import relativedelta
import csv
import urllib.request
from bs4 import BeautifulSoup

today = datetime.date.today()
yesterday = today + relativedelta(days=-5)

print(yesterday)