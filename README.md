# cryoto_currency_Automatic
This is an automatic trading bot for crypto.


pythonの外部ライブラリであるccxtを利用した、仮想通貨交換所Coincheckで自動売買を行うプログラムです。
ゴールデンクロスが発生したら、指定の数量で成行買い注文を発注する単純な仕様となっています。

利用方法:
Coincheck.py, line_notify.py に発行したAPIキーを記載し、exec.pyで実行します。
うまくいけば、ゴールデンクロスが発生した際に、買い注文が行われ、Lineに通知が行きます。
エラーが生じた場合も、Lineに通知がいき、終了となります。

備考:
取引対象(symbol)は"MONA/JPY"なっていますが、取り扱いのある通貨ペアであれば、書き換えることで、取引が可能になります。
その際は、最低注文数量に注意してください。（例:ビットコインは0.005BTC以上かつ500円以上の取引から有効等）
