# -*- coding: utf-8 -*-
import os
import datetime
from dateutil.relativedelta import relativedelta
import csv
import urllib.request
from bs4 import BeautifulSoup

# CSVいらない疑惑

today = datetime.date.today()
yesterday = today + relativedelta(days=-1)


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

    # ボツ1
    #    tags = soup.find_all('tr', class_='mtx')
    #    tbs = [tag.text for tag in tags]

    # ボツ2
    #    for tr in trs.find_all("tr")[2:]:
    #        tds = tr.find_all("td")

    trs = soup.find_all("tr", class_="mtx")[3:]

    for tr in trs:
        tds = tr.find_all("td")
        if tds[1].string is None:
            break

        data_list.append(date)
        data_list.append(tds[0].string)
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

    # データ取得開始・終了日
    start_date = datetime.date(2022, 1, 1)  # あとで出穂の日からに直す
    end_date = yesterday  # 気象庁の更新が昨日までなので

    # CSV の列
    fields = [
        "日",
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
        "最深積雪(m)"
    ]

    with open(os.path.join(output_dir, output_file), "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(fields)
        date = start_date

        while date != end_date + datetime.timedelta(1):  #
            
        for mon in range(1,13):

            # 鶴岡市
            # base_url = (
            #     "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=35&block_no=0263&year=2022&month=01&day=1&view="
                        )
            search_url = (
                f"https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=35&block_no=0263&year=2022&month={mon}&day=1&view="
                        )

            data_per_day = scraping(search_url, date)

            for dpd in data_per_day:
                writer.writerow(dpd)

            relativedelta(months=1)


if __name__ == "__main__":
    create_csv()
