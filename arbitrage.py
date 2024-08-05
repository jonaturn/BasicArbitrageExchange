# arbitrage.py

from exchange import get_price, place_order

def find_arbitrage_opportunity(exchange1, exchange2, symbol, amount):
    bid1, ask1 = get_price(exchange1, symbol)
    bid2, ask2 = get_price(exchange2, symbol)

    if bid1 > ask2:
        print(f'Arbitrage opportunity! Buy on exchange2 at {ask2} and sell on exchange1 at {bid1}')
        place_order(exchange2, symbol, 'limit', 'buy', amount, ask2)
        place_order(exchange1, symbol, 'limit', 'sell', amount, bid1)
    elif bid2 > ask1:
        print(f'Arbitrage opportunity! Buy on exchange1 at {ask1} and sell on exchange2 at {bid2}')
        place_order(exchange1, symbol, 'limit', 'buy', amount, ask1)
        place_order(exchange2, symbol, 'limit', 'sell', amount, bid2)
    else:
        print('No arbitrage opportunity found.')