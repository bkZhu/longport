import os

import akshare as ak

from common.Utils import disk_load_df_data, save_df_to_csv


def query_min_data(symbol: str):
    """
    查询近5个交易日的分钟级数据，如果需要更多的数据，只能每周定时拉取，保存在本地
    :param symbol: 注意和长桥的symbol有一些区别
    :return: df
    """
    return ak.stock_us_hist_min_em(symbol=symbol)

def load_biz_data(symbol: str):
    """
    查询天级数据
    :param symbol: 注意和长桥的symbol有一些区别
    :return: df
    """
    return ak.stock_us_hist(symbol=symbol, period="daily",
                            start_date="20200101", end_date="21240214")

def load_all_us_stock_real_time():
    """
    查询所有美股实时价格，时效性有待验证
    :return: df
    """
    return ak.stock_us_spot_em()


PDD = "105.PDD"
NVDA = "105.NVDA"