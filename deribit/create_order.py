import ccxt
from setting import api_key, secret


deribit = ccxt.deribit({
    'apiKey': api_key,
    'secret': secret,
    'urls': {'api': 'https://test.deribit.com'},

})


# print(exchange.fetch_balance())
symbol = 'BTC-PERPETUAL'
type = 'market'
side = 'sell'
amount = 100 / 10   #post的order size 为amount的10倍， 不知道为什么..
price = None
params = {

}

order = deribit.create_order(symbol, type, side, amount, price, params)

print(order)
