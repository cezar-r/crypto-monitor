from kucoin.client import Client

API_SECRET = "a438c1ff-4e61-4154-a3b9-acb9fb54e6cc"
API_KEY = "61760bb6eaa68500012b8e44"
PASSPHRASE = "Tennis123-"


client = Client(API_KEY, API_SECRET, PASSPHRASE)

class KuCoinAPI:

	def get_price(ticker):
		price = client.get_order_book(f'{ticker}-USDT')['bids'][0][0]
		return price





