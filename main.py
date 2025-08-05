# 
import os
import time
from datetime import datetime

# Third-party packages
import requests
from binance.client import Client
from dotenv import load_dotenv

def run_loop(client: Client):
    while True:
        print(f"[{datetime.now()}]:", get_price(client))
        time.sleep(600)

def main():
    load_dotenv()
    api_key = os.environ["BINANCE_SECRET_TEST"]
    api_secret = os.environ["BINANCE_SECRET_KEY"]

    client = Client(api_key, api_secret, testnet=True)
    run_loop(client)

def get_price(client: Client):
    tk = client.get_orderbook_ticker(symbol="BTCUSDC")
    return float(tk["bidPrice"]), float(tk["askPrice"])


if __name__ == "__main__":
    main()

# End of file