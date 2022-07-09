# -*- coding: utf-8 -*-
import os
import datetime
from dateutil.relativedelta import relativedelta
import csv
import urllib.request
from bs4 import BeautifulSoup


# CSVいらない疑惑i
# データ取得開始・終了日
yesterday = datetime.datetime.today() - relativedelta(days=1)  # 気象庁の更新が昨日までなので
end_month = yesterday.month
# 日付条件の設定
strdt = datetime.datetime.strptime("2022-01-01", "%Y-%m-%d")  # 開始日


def str2float(weather_data):
    try:
        return float(weather_data)
    except ValueError:  # 例外処理
        return 0


def scraping2(url, mon):  # mon
    # 気象データのページを取得
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    trs = soup.find("table", {"class": "data2_s"})

    data_list = []
    data_list_per_hour = []

    # table の中身を取得
    trs = soup.find_all("tr", class_="mtx")[3:]
    for tr in trs:
        tds = tr.find_all("td")
        ths = tr.find_all("th")  # 要素の取得の書き方聞く
        if tds[1].string == "///":
            break

        data_list.append("1991～2020")
        data_list.append(f"{mon}月{ths}")  # 要素の取得の書き方聞く
        data_list.append(str2float(tds[0].string))
        data_list.append(str2float(tds[1].string))
        data_list.append(str2float(tds[2].string))
        data_list.append(str2float(tds[3].string))
        data_list.append(str2float(tds[4].string))
        data_list.append(str2float(tds[5].string))
        data_list.append(str2float(tds[6].string))

        data_list_per_hour.append(data_list)

        data_list = []

    return data_list_per_hour


def create_csv():
    # CSV 出力先ディレクトリ
    output_dir = r"C:\Users\user\Desktop\camp"

    # 出力ファイル名
    output_file = "normal value.temperature.csv"

    # CSV の列
    fields = [
        "統計期間",
        "月日",
        "降水量(mm)",
        "平均気温(℃)",
        "日最高気温(℃)",
        "日最低気温(℃)",
        "日照時間(h)",
        "降雪の深さ合計(cm)",
        "最深積雪(cm)",
    ]

    with open(os.path.join(output_dir, output_file), "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(fields)
        for mon in range(1, 13):  # URLのmonth==〇〇にいれる変数とりあえずrangeで
            # year=2022の部分も改良の余地ありあとで
            search_url = f"https://ds.data.jma.go.jp/obd/stats/etrn/view/nml_amd_d.php?prec_no=35&block_no=0263&year=2022&month={mon}&day=06&view=g_tem"
            data_per_day = scraping2(search_url, mon)
            for dpd in data_per_day:
                writer.writerow(dpd)
                if mon == 12:  # 12/1までになっているので and day == 31: あとで足す
                    break


if __name__ == "__main__":
    create_csv()
