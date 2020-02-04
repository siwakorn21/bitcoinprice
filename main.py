import requests
import time

TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'


def get_latest_crypto_price(crypto):

    response = requests.get(TICKER_API_URL + crypto)
    response_json = response.json()

    # [{'id': 'bitcoin', 'name': 'Bitcoin',
    # 'symbol': 'BTC', 'rank': '1', 'price_usd': '8774.31051566',
    # 'price_btc': '1.0', '24h_volume_usd': '25892948782.7', 'market_cap_usd': '159558423792',
    # 'available_supply': '18184725.0', 'total_supply': '18184725.0', 'max_supply': '21000000.0', 'percent_change_1h': '0.31',
    # 'percent_change_24h': '3.64', 'percent_change_7d': '1.42', 'last_updated': '1580138736'}]

    return float(response_json[0]['price_usd'])


def get_localtime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


def main():

    last_price = -1

    while True:
        crypto = 'bitcoin'
        price = get_latest_crypto_price(crypto)
        if (last_price != price):
            print('Bitcoin price in usd : ', price)
            print("local time in Thailand: ", get_localtime())
            print("PRICE FROM CoinMarketCap")
            print("------------------------------")
            last_price = price


main()
