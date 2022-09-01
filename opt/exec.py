import pandas as pd
import sys
import traceback
from line_notify import LineNotify
from pprint import pprint
from Coincheck import CoinCheck
from Analysis import get_candles,make_sma
import time


base = CoinCheck() #CoinCheckのインスタンスを生成
symbol = "MONA/JPY" #通貨ペアを指定(なお,coincheckでは、0.005btc以上かつ500JPY以上の発注でないとエラー)
amount = 500        #注文量(日本円)

line_notify = LineNotify()
line_notify.send("Start Trading")

print("Start Trading")

# Botを起動
while True:
    try:
        candles = get_candles("minute",1000).set_index("Time")
        sma_5 = make_sma(candles,5) #短期移動平均線の生成
        sma_13 = make_sma(candles,13) #長期移動平均線の生成

        # 短期移動平均線　> 長期移動平均線　の状態が３本連続で続いたら
        golden_cross = sma_5.iloc[-1] > sma_13.iloc[-1] \
            and sma_5.iloc[-2] > sma_13.iloc[-2] \
            and sma_5.iloc[-3] > sma_13.iloc[-3] \
            and sma_5.iloc[-4] < sma_13.iloc[-4]
        
        dead_cross = sma_5.iloc[-1] < sma_13.iloc[-1] \
            and sma_5.iloc[-2] < sma_13.iloc[-2] \
            and sma_5.iloc[-3] < sma_13.iloc[-3] \
            and sma_5.iloc[-4] > sma_13.iloc[-4]
        
        # 現在のポジションを取得する必要はなし.Coincheckの場合はget_balanceで
        # position = base.get_position(symbol)
        balance = base.get_balance("JPY")

        if balance["free"] >= 500: #口座に日本円が十分にある場合は
            if golden_cross:
                order = base.create_order(symbol, "market", "buy", amount)
                #price = order["price"]
                line_notify.send(f"{amount}円の買いを注文しました.")
                break
            
            """
            elif dead_cross: # ノーポジかつデッドクロスなら売り注文
                order = base.create_order(symbol, "market", "sell", amount)
                price = order["price"]
                line_notify.send(f"{price} で買いを注文しました.")
            """

        time.sleep(30)
    except:
        line_notify.send(traceback.format_exc())
        sys.exit()

sys.exit()