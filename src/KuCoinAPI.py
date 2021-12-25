#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File containing the KuCoin API object
"""

from kucoin.client import Client

API_SECRET = "<api_secret>"
API_KEY = "<api_key>"
PASSPHRASE = "<passphrase>"


client = Client(API_KEY, API_SECRET, PASSPHRASE)

class KuCoinAPI:
	"""A class representing the KuCoinAPI"""
	def get_price(ticker):
		"""
		Method that gets the price of a ticker
		
		Parameters
		----------
		ticker : str
			Ticker of the given crypto
		
		Returns
		-------
		price : float
			price of ticker
		"""
		price = client.get_order_book(f'{ticker}-USDT')['bids'][0][0]
		return price





