import ccxt
from setting import api_key,secret

exchange = ccxt.bitmex({
    'apiKey' : api_key,
    'secret' : secret,
    'urls' : {'api': 'https://testnet.bitmex.com'},
    'enableRateLimit': True,
    'options': {
           
        'api-expires': 60, 
    },
    
})

symbol = 'BTC/USD'
type = 'market'
side = 'sell'
amount = 100
price = None
params = {

}

order = exchange.create_order(symbol,type,side,amount,price,params)

print(order)
