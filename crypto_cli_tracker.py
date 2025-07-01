import requests
import argparse

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if coin_id in data:
            price = data[coin_id]["usd"]
            print(f"The current price of {coin_id.upper()} is: ${price}")
        else:
            print("Invalid coin name.")
    else:
        print("Something went wrong. Try again later.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crypto CLI Tracker")
    parser.add_argument("coin", help="Enter a crypto coin name like bitcoin or ethereum")
    args = parser.parse_args()
    get_price(args.coin)
