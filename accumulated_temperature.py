from socket import if_nameindex
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


def accumulated():
    with open("average_temperature.csv", encoding="cp932") as f:
        # 不要なコメント部分を読み込まないようにする
        next(f)
        reader = csv.reader(f)  # ヘッダーから読み込み開始

        # 方法①
        rows_data = []  # 全体のデータ配列の初期化
        for row in reader:  # 1行ずつをrowとして取得
            row_data = []  # 1行のデータ配列を初期化
            for data in row:  # 1列ずつをdataとして取得
                row_data.append(data)  # 各dataは1行のデータ配列に追加
            rows_data.append(row_data)  # 1行のデータ配列を全体のデータ配列に追加

        print(rows_data)  # 全体を取得

#        transpose = []
#        for i in range(len(roes_date[0])):
#            tmp = []
#            for v in roes_date:
#                tmp.append(v[i])
#            transpose.append(tmp)


with open("normal_value.temperature.csv", encoding="cp932") as f:
    # 不要なコメント部分を読み込まないようにする
    next(f)
    reader = csv.reader(f)  # ヘッダーから読み込み開始

    # 方法①
    roes_date2 = []  # 全体のデータ配列の初期化
    for row in reader:  # 1行ずつをrowとして取得
        row_data = []  # 1行のデータ配列を初期化
        for data in row:  # 1列ずつをdataとして取得
            row_data.append(data)  # 各dataは1行のデータ配列に追加
            roes_date2.append(row_data)  # 1行のデータ配列を全体のデータ配列に追加
# print(roes_date2)  # 全体を取得

if __name__ == "__main__":
    accumulated()
