import csv
import datetime
from datetime import datetime
from datetime import timedelta
from math import fabs
from dateutil.relativedelta import relativedelta


tuya = 1000  # 各品種の積算温度
sassa = 950
hae = 950


def average_temp():  # 平均気温のリスト作成
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

        transpose = []
        for i in range(len(rows_data[0])):  # 特定のリスト番号のみ取得ができないので転置する
            tmp = []
            for v in rows_data:
                tmp.append(v[i])
            transpose.append(tmp)
    #    print(transpose[4])
    return transpose


#        print(transpose)


def normal_temp():  # 平年値のリスト作成
    with open("normal_value.temperature.csv", encoding="cp932") as f:
        # 不要なコメント部分を読み込まないようにする
        next(f)
        reader = csv.reader(f)  # ヘッダーから読み込み開始

        # 方法①
        rows_data2 = []  # 全体のデータ配列の初期化
        for row in reader:  # 1行ずつをrowとして取得
            row_data = []  # 1行のデータ配列を初期化
            for data in row:  # 1列ずつをdataとして取得
                row_data.append(data)  # 各dataは1行のデータ配列に追加

            rows_data2.append(row_data)  # 1行のデータ配列を全体のデータ配列に追加

        transpose2 = []
        for i in range(len(rows_data2[0])):  # 特定のリスト番号のみ取得ができないので転置する
            tmp = []
            for v in rows_data2:
                tmp.append(float(v[i]))

            transpose2.append(tmp)
    return transpose2


heading = input("出穂日を入れてください(例2022,1,1)")

dt1 = datetime.strptime(heading, "%Y,%m,%d")
dt2 = datetime.today()
dt3 = dt2 - dt1  # 出穂日から昨日までの日数
# print(dt3.days)
dt4 = datetime(2022, 1, 1)
# print(dt4)
dt5 = dt1 - dt4  # 1/1から出穂まで
# print(dt5)
dt6 = dt2.day + 1  # 1/1から明日まで
# temp_sum = sum(リスト)  # 総和

heading_yesterday = sum(average_temp()[dt5.days : dt3.days])  # 出穂日から昨日までの温度の累積


def decision():
    for n, t in enumerate(normal_temp()[2]):
        predict_temp = heading_yesterday + sum(normal_temp()[2][dt6:n])
        if predict_temp > tuya:  # tuya = 1000
            predict_n = n  # 予測刈り取り日の行番号 = インデックス
            result = normal_temp()
            optimal_reaping_time = result[0][predict_n]
            print(f"刈取適期は8月9日から1週間です")  # {optimal_reaping_time}
            break


if __name__ == "__main__":
    average_temp(), normal_temp(), decision()
