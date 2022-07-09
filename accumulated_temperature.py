import pandas as pd
from datetime import date
import os
import datetime
from dateutil.relativedelta import relativedelta
import csv
import urllib.request
from bs4 import BeautifulSoup
import normal_value_temperature
import average_temperature


def average_temperatures():
    for mon in range(1, 13):
        aver = average_temperature.scraping(
            f"https://ds.data.jma.go.jp/obd/stats/etrn/view/nml_amd_d.php?prec_no=35&block_no=0263&year=2022&month={mon}&day=06&view=g_tem",
            mon,
        )
        return aver


def normal_value_temperatures():
    for mon in range(1, 13):
        norm = normal_value_temperature.scraping2(
            f"https://ds.data.jma.go.jp/obd/stats/etrn/view/nml_amd_d.php?prec_no=35&block_no=0263&year=2022&month={mon}&day=06&view=g_tem",
            mon,
        )
        return norm
