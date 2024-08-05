

import ccxt

def create_exchange(exchange_name, api_key, secret):
    exchange_class = getattr(ccxt, exchange_name)
    return exchange_class({
        'apiKey': api_key,
        'secret': secret,
    })

def get_price(exchange, symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['bid'], ticker['ask']

def place_order(exchange, symbol, order_type, side, amount, price=None):
    if order_type == 'market':
        order = exchange.create_market_order(symbol, side, amount)
    elif order_type == 'limit':
        order = exchange.create_limit_order(symbol, side, amount, price)
    return order