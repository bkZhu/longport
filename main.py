import json

from longport.openapi import Config, TradeContext, QuoteContext, PushQuote, SubType

file = open('E://work//QuantLongPort//code//longPortProject//env.txt', 'r')
envMap = json.loads(file.read())
app_key = envMap["LONGPORT_APP_KEY"]
app_secret = envMap["LONGPORT_APP_SECRET"]
access_token = envMap["LONGPORT_ACCESS_TOKEN"]
config = Config(app_key=app_key, app_secret=app_secret, access_token=access_token)
#订单
tradeCtx = TradeContext(config)

#行情
def on_quote(symbol: str, event: PushQuote):
    print(symbol, event)
quoteCtx = QuoteContext(config)
quoteCtx.set_on_quote(on_quote)

if __name__ == '__main__':
    # resp = tradeCtx.account_balance()
    # print(resp)
    ctx = quoteCtx
    resp = ctx.static_info(["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"])
    print(resp)



