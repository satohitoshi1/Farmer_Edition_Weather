import csv


def average():
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
        print(transpose)


def normal():
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

        transpose = []
        for i in range(len(rows_data2[0])):  # 特定のリスト番号のみ取得ができないので転置する
            tmp = []
            for v in rows_data2:
                tmp.append(v[i])
            transpose.append(tmp)
        print(transpose)


if __name__ == "__main__":
    average(), normal()
