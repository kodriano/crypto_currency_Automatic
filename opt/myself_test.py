# bybitからマーケット情報を取得して、ラインに送るプログラム

import ccxt
from pprint import pprint
from line_notify import LineNotify
from bb_api import BbApi

base = BbApi()
symbol = "BTC/USD" # 通貨ペア
amount = 0.1         # 注文量(USD)

position = base.get_position(symbol)

line_notify = LineNotify()
line_notify.send(f"テスト送信です.:{position}")

"""
order = base.create_order(symbol, "market", "buy", amount)
price = order["price"]
line_notify.send(f"Buy on the market {price}")
pprint(order)
"""