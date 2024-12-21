import os

import pandas as pd


def save_df_to_csv(df_data, relative_data_path, file_name):
    # 获取数据存放位置
    absolute_data_path = os.path.abspath(relative_data_path)
    # 构建完整的 CSV 文件路径
    csv_file_path = os.path.join(absolute_data_path, file_name)
    print("save file path:", csv_file_path)

    # 检查路径是否存在，如果不存在则创建
    if not os.path.exists(absolute_data_path):
        print(f"The path {absolute_data_path} does not exist. Creating it...")
        os.makedirs(absolute_data_path)

    # 检查路径是否确实是一个目录
    if os.path.isdir(absolute_data_path):
        # 保存 DataFrame 到 CSV
        df_data.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
        # print(f"Data saved to {csv_file_path}")
    else:
        print(f"The path {absolute_data_path} is not a directory.")


def disk_load_df_data(relative_data_path, file_name):
    # 获取数据存放位置
    absolute_data_path = os.path.abspath(relative_data_path)
    # 构建完整的 CSV 文件路径
    csv_file_path = os.path.join(absolute_data_path, file_name)
    # print("load file path:", csv_file_path)

    # 检查文件是否存在
    if not os.path.exists(csv_file_path):
        # print(f"The file {csv_file_path} does not exist!!")
        return None  # 或者抛出异常
    else:
        try:
            df_data_load = pd.read_csv(csv_file_path, encoding='utf-8-sig')  # 假设使用 utf-8-sig 编码
            return df_data_load
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None  # 或者重新抛出异常