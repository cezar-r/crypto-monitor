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
		for prev_timestamp in list(self.prices.keys())[::-1]:
			if price/self.prices[prev_timestamp] <= .97:
				self.prices = {}
				return price, self.prices[prev_timestamp], int((timestamp -  prev_timestamp).total_seconds() * 60), False
			elif price/self.prices[prev_timestamp] >= 1.03:
				self.prices = {}
				return price, self.prices[prev_timestamp], int((timestamp -  prev_timestamp).total_seconds() * 60), True
			self.noti = False
		self.prices[timestamp] = price
		return False, False, False, False
				


if __name__ == '__main__':
	while True:
		btc = Crypto('BTC')
		btc.check()
		time.sleep(60)