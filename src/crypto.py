#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File containing the Crypto object
"""

import time
from datetime import datetime, timedelta
from KuCoinAPI import KuCoinAPI

kucoin = KuCoinAPI

class Crypto():
	"""
	A class representing a crypto
	
	Attributes
	----------
	ticker : str
		Ticker of crypto
	prices : dict
		Dictionary of prices: {timestamp, price}
	"""
	def __init__(self, ticker):
		self.ticker = ticker.upper()
		self.prices = {}

	def check(self):
		"""
		Method that checks if there was a significant price difference
		
		Returns
		-------
		price : float
			Current price of crypto
		prev_price : float
			Price of crypto that started the significant price move
		int
			number of minutes that price move took
		bool
			Whether or not the price went up
		If no price move, return False for everything 
		"""
		if len(list(self.prices.keys())) == 1440:
			del self.prices[(list(self.prices.keys()))[0]]
		price = float(kucoin.get_price(self.ticker))
		timestamp = datetime.now()
		print('')
		print(self.ticker, '-', price)
		print(f'Entries: {len(list(self.prices.keys()))}')
		for prev_timestamp, prev_price in list(self.prices.items())[::-1]:
			if price/prev_price <= .95:
				self.prices = {}
				return price, prev_price, int((timestamp -  prev_timestamp).total_seconds() / 60), False
			elif price/prev_price >= 1.05:
				self.prices = {}
				return price, prev_price, int((timestamp -  prev_timestamp).total_seconds() / 60), True
		self.prices[timestamp] = price
		return False, False, False, False
				
