import ccxt
from pprint import pprint
from line_notify import LineNotify

API_KEY = "取得したコインチェックのAPIキーを入れる."
SECRET = "取得したシークレットキーを入れる。"

class CoinCheck:
    def __init__(self):
        self.base = ccxt.coincheck(
            {
                'apiKey': API_KEY,
                'secret': SECRET,
            }
        )
    
    def get_position(self,symbol):
        self.base.load_markets()
        market = self.base.market(symbol)

        return self.base.v2_private_get_position_list({"symbol":market["id"]})["result"]
    
    def create_order(self,symbol,order_type, side, amount):
        order = self.base.createOrder(
            symbol,     #通貨ペア
            order_type, #成行か指値か(market:成行,limit:指値)
            side,       #買いか売りか(buy:買い, sell:売り)
            amount,     #注文量(JPY)
            {
                "qty": amount
            }
        )

        return order

    def get_balance(self,currency):
        balances = self.base.fetch_balance()
        return balances[currency]

"""
exchange = CoinCheck()
balances = exchange.get_balance("JPY")

# coincheckの最小注文量が、0.005BTC以上かつ500円以上だったのでエラーが多発した.

order = exchange.create_order("MONA/JPY","market","buy",550)
print(balances["free"])
pprint(order)
"""

"""
line_notify = LineNotify()
for key in balances.items():
    print(key)
    break
    #line_notify.send(f"テスト送信です。:{key}")
"""
