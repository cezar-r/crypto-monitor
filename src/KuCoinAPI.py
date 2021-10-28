from kucoin.client import Client

API_SECRET = "<api_secret>"
API_KEY = "<api_key>"
PASSPHRASE = "<passphrase>"


client = Client(API_KEY, API_SECRET, PASSPHRASE)

class KuCoinAPI:

	def get_price(ticker):
		price = client.get_order_book(f'{ticker}-USDT')['bids'][0][0]
		return price





