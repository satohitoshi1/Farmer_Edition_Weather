# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import csv
import urllib.request
from bs4 import BeautifulSoup


# CSVいらない疑惑
# データ取得開始・終了日
yesterday = dt.date.today() - relativedelta(days=1)  # 気象庁の更新が昨日までなので
end_month = yesterday.month
# 日付条件の設定
strdt = dt.strptime("2022-01-01", "%Y-%m-%d")  # 開始日
enddt = dt.strptime(yesterday, "%Y-%m-%d")  # 終了日

# 日付差の日数を算出（リストに最終日も含めたいので、＋１しています）
days_num = (enddt - strdt).days + 1
# シンプルにforとappendを使用した場合
datelist = []
for writing in range(days_num):
    datelist.append(strdt + timedelta(days=writing))


def str2float(weather_data):
    try:
        return float(weather_data)
    except ValueError:  # 例外処理
        return 0


def scraping(url, date):
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
        if tds[1].string is None:
            break

        data_list.append(datelist)
        data_list.append(str2float(tds[1].string))
        data_list.append(str2float(tds[2].string))
        data_list.append(str2float(tds[3].string))
        data_list.append(str2float(tds[4].string))
        data_list.append(str2float(tds[5].string))
        data_list.append(str2float(tds[6].string))
        data_list.append(str2float(tds[7].string))
        data_list.append(str2float(tds[8].string))
        data_list.append(str2float(tds[9].string))
        data_list.append(str2float(tds[10].string))
        data_list.append(str2float(tds[11].string))
        data_list.append(str2float(tds[12].string))
        data_list.append(str2float(tds[13].string))
        data_list.append(str2float(tds[14].string))
        data_list.append(str2float(tds[15].string))
        data_list.append(str2float(tds[16].string))
        data_list.append(str2float(tds[17].string))

        data_list_per_hour.append(data_list)

        data_list = []

    return data_list_per_hour


def create_csv():
    # CSV 出力先ディレクトリ
    output_dir = r"C:\Users\user\Desktop\camp"

    # 出力ファイル名
    output_file = "weather.csv"

    # CSV の列
    fields = [
        "年月日",
        "降水量(合計/mm)",
        "降水量(最大1時間/mm)",
        "降水量(最大10分間/mm)",
        "平均気温(℃)",
        "最高気温(℃)",
        "最低気温(℃)",
        "平均湿度(㌫)",
        "最小湿度(㌫)",
        "平均風速(m/s)",
        "最大風速(m/s)",
        "風向",
        "最大瞬間風速(m/s)",
        "風向",
        "最多風向",
        "日照時間(h)",
        "降雪の深さの合計(m)",
        "最深積雪(m)",
    ]

    with open(os.path.join(output_dir, output_file), "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(fields)
        for mon in range(1, end_month + 1):  # URLのmonth==〇〇にいれる変数とりあえずrangeで
            # 鶴岡市
            # base_url = (
            #     "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=35&block_no=0263&year=2022&month=01&day=1&view="
            #            ) # year=2022の部分も改良の余地ありあとで
            search_url = f"https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=35&block_no=0263&year=2022&month={mon}&day=1&view="
            data_per_day = scraping(search_url, strdt)
            for dpd in data_per_day:
                writer.writerow(dpd)
            if mon == end_month:
                break


if __name__ == "__main__":
    create_csv()
