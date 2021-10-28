import time
from datetime import datetime, timedelta
from KuCoinAPI import KuCoinAPI

kucoin = KuCoinAPI

class Crypto():

	def __init__(self, ticker):
		self.ticker = ticker.upper()
		self.prices = {}

	def check(self):
		if len(list(self.prices.keys())) == 1440:
			del self.prices[(list(self.prices.keys()))[0]]
		price = float(kucoin.get_price(self.ticker))
		timestamp = datetime.now()
		print('')
		print(self.ticker, '-', price)
		print(f'Entries: {len(list(self.prices.keys()))}')
		for prev_timestamp, prev_price in list(self.prices.items())[::-1]:
			if price/prev_price <= .97:
				self.prices = {}
				return price, prev_price, int((timestamp -  prev_timestamp).total_seconds() / 60), False
			elif price/prev_price >= 1.03:
				self.prices = {}
				return price, prev_price, int((timestamp -  prev_timestamp).total_seconds() / 60), True
		self.prices[timestamp] = price
		return False, False, False, False
				
