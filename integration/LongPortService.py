import datetime
from decimal import Decimal

from longport.openapi import OrderType, OrderSide, TimeInForceType, Market, OrderStatus

from main import tradeCtx

def buyLimit(symbol: str, quantity: int, buy_price: float):
    """
    买限价单
    :param symbol:
    :param quantity:
    :param price:
    :return:
    """
    return tradeCtx.submit_order(
    symbol,
    OrderType.LO,
    OrderSide.Buy,
    Decimal(quantity),
    TimeInForceType.Day,
    submitted_price=Decimal(buy_price))

def buyMarket(symbol: str, quantity: int, buy_price: float):
    """
    买市单价
    :param symbol:
    :param quantity:
    :param price:
    :return:
    """
    return tradeCtx.submit_order(
    symbol,
    OrderType.MO,
    OrderSide.Buy,
    Decimal(quantity),
    TimeInForceType.Day,
    submitted_price=Decimal(buy_price))

def sellLimit(symbol: str, quantity: int):
    """
    卖限价单，可能会因为价格波动导致滑单
    :param symbol:
    :param quantity:
    :return:
    """
    return tradeCtx.submit_order(
    symbol,
    OrderType.LO,
    OrderSide.Sell,
    Decimal(quantity),
    TimeInForceType.Day)

def sellMarket(symbol: str, quantity: int):
    """
    卖市价单，需要保证卖出时，使用此方法
    :param symbol:
    :param quantity:
    :return:
    """
    return tradeCtx.submit_order(
    symbol,
    OrderType.MO,
    OrderSide.Sell,
    Decimal(quantity),
    TimeInForceType.Day)

def sellLit(symbol: str, quantity: int, trigger_price: float, sell_price: float):
    """
    止盈止损，触价卖出限价单
    :param symbol:
    :param quantity:
    :param trigger_price:
    :param sell_price:
    :return:
    """
    return tradeCtx.submit_order(
        symbol,
        OrderType.LIT,
        OrderSide.Sell,
        Decimal(quantity),
        TimeInForceType.GoodTilCanceled,
        Decimal(sell_price),
        trigger_price=Decimal(trigger_price))

def sellTslp(symbol: str, quantity: int, trailing_percent: float, limit_offset: float):
    """
    回落卖出
    :param symbol:
    :param quantity:
    :param trailing_percent: 回落百分比，注意0.5表示0.5%
    :param limit_offset: 减价额度
    :return:
    """
    now = datetime.datetime.now() + datetime.timedelta(days=1)
    year = now.year
    month = now.month
    day = now.day
    return tradeCtx.submit_order(
    symbol,
    OrderType.TSLPPCT,
    OrderSide.Sell,
    Decimal(quantity),
    TimeInForceType.GoodTilDate,
    expire_date=datetime.date(year, month, day),
    trailing_percent=Decimal(trailing_percent),
    limit_offset=Decimal(limit_offset)
)

def buyTslp(symbol: str, quantity: int, trailing_percent: float, limit_offset: float):
    """
    反弹买入
    :param symbol:
    :param quantity:
    :param trailing_percent: 反弹百分比，注意0.5表示0.5%
    :param limit_offset: 加价额度
    :return:
    """
    now = datetime.datetime.now() + datetime.timedelta(days=1)
    year = now.year
    month = now.month
    day = now.day
    return tradeCtx.submit_order(
    symbol,
    OrderType.TSLPPCT,
    OrderSide.Buy,
    Decimal(quantity),
    TimeInForceType.GoodTilDate,
    expire_date=datetime.date(year, month, day),
    trailing_percent=Decimal(trailing_percent),
    limit_offset=Decimal(limit_offset)
)

def cancel_order(order_id: str):
    return tradeCtx.cancel_order(order_id)

def is_buy_order_not_fill(order_id: str):
    """
    检查订单是否已经完成，如果处于new 已委托状态，表明没有成交，如果没有，可视为
    :param order_id:
    :return:
    """
    return len(tradeCtx.today_orders(
        status=[OrderStatus.Filled, OrderStatus.Filled],
        side=OrderSide.Buy,
        market=Market.US,
        order_id=order_id)) > 0


if __name__ == '__main__':
    symbol = "NVDA.US"
    quantity = 100
    buy_price = 100
    trailing_percent = 0.5
    resp = buyTslp(symbol, quantity, 0.5, 1)
    print(resp.order_id)