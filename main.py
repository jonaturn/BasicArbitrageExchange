# main.py
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

import time
from exchange import create_exchange
from exchange import find_arbitrage_opportunity

def main():
    binance = create_exchange('binance', os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_SECRET'))
    kraken = create_exchange('kraken', os.getenv('KRAKEN_API_KEY'), os.getenv('KRAKEN_SECRET'))
    symbol = 'BTC/USDT'
    amount = 0.01  # Amount of BTC to trade

    while True:
        try:
            find_arbitrage_opportunity(binance, kraken, symbol, amount)
            time.sleep(1)  # Wait a bit before checking again
        except Exception as e:
            print(f'Error: {e}')
            time.sleep(5)  # Wait before retrying in case of an error

if __name__ == "__main__":
    main()