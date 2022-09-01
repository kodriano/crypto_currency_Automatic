import pandas as pd
pd.options.display.float_format = '{:.2f}'.format

import requests
import time
import sys
import traceback
from datetime import datetime

# CryptoCompareからBTC/JPYのヒストリカルデータを取得しローソク足を生成
def get_candles(timeframe,limit):
    # timeframe(時間軸)には[minute],[hour],[day]のいずれかが入る
    base_url = f"https://min-api.cryptocompare.com/data/histo{timeframe}"

    params = {
        "fsym": "MONA",
        "tsym": "JPY",
        "limit": limit,
    }

    # ↓ここはwebの知識も浅いので要勉強
    res = requests.get(base_url,params,timeout=10).json()

    time, open, high, low, close = [],[],[],[],[]

    for i in res["Data"]:
        time.append(datetime.fromtimestamp(i["time"]))
        open.append(i["open"])
        high.append(i["high"])
        low.append(i["low"])
        close.append(i["close"])

    candles = pd.DataFrame(
        {
            "Time": time,
            "Open": open,
            "High": high,
            "Low" : low,
            "Close": close
        }
    )

    return candles

#単純移動平均線の算出
def make_sma(candles, span):
    return pd.Series(candles["Close"]).rolling(window = span).mean()

