import os

from common.Utils import disk_load_df_data, save_df_to_csv
from integration.AkShareService import query_min_data


"""
基于query_min_data()落近5天分钟级数据
"""

def save_data():
    df = disk_load_df_data("../task/", "美股实时行情.csv")
    # 打开失败记录文件，准备写入
    with open("../task/fail.txt", 'a') as fail_file:
        for i, symbol in enumerate(df["代码"].values):
            try:
                file_name = symbol + ".csv"
                file_path = "./美股实时行情/" + file_name
                # 检查文件是否存在
                if not os.path.exists(file_path):
                    min_df = query_min_data(symbol)
                    save_df_to_csv(min_df, "./美股实时行情/", file_name)
                    process = i / len(df) * 100
                    print(file_name + " done " + "{:.2f}".format(process) + "%")
                else:
                    print(file_name + " already exists, skipped.")
            except Exception as e:
                # 将失败的symbol写入失败记录文件
                fail_file.write(symbol + "\n")
                print(symbol + " failed due to: " + str(e))

def retry_fail_data():
    with open("./fail.txt", 'r') as fail_file:  # 使用 'r' 模式读取文件
        for i, symbol in enumerate(fail_file):  # 迭代每一行
            symbol = symbol.strip()
            print(symbol + " retry...")
            file_name = symbol + ".csv"
            min_df = query_min_data(symbol)
            save_df_to_csv(min_df, "./美股实时行情/", file_name)
            print(file_name + " done")
    return

if __name__ == '__main__':
    print("---------pulling data---------")
    # save_data()
    # retry_fail_data()
