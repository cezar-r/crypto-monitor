#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File containing the Alerts object
"""
import time
from datetime import datetime
from twilio.rest import Client
from crypto import Crypto

MYNUMBER = '<my_number>'
account_sid = '<account_sid>'
auth_token = '<auth_token>'
client = Client(account_sid, auth_token)

CRYPTOS = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT', 'LINK', 'COTI', 'LTC', 'SHIB', 'ALGO']

reciever = []
DELAY = 60 # seconds


class Alerts:
	"""
	A class representing the alert system
	
	Attributes
	----------
	coins : dict
		Dictionary of ticker symbols and coin objets
	"""
	def __init__(self):
		self.coins = {}
		for ticker in CRYPTOS:
			coin = Crypto(ticker)
			self.coins[ticker] = coin
		# self._send_all(reciever, 'Crypto alerts in bound')
		self.run()

	def run(self):
		"""Method that runs the monitor"""
		while True:
			for ticker, coin in list(self.coins.items()):
				self._request(ticker, coin)
			print(f'|{datetime.now()}|')
			time.sleep(DELAY)


	def _request(self, ticker, coin):
		"""Method that requests the price of a given coin"""
		try:
			price, prev_price, timestamp, up = coin.check()
			if price:
				self.send_msg(ticker, price, prev_price, timestamp, up)
		except Exception as e:
			print(f'|{datetime.now()}|Exception: {str(e)}, sleeping 60 sec |{ticker} ')
			time.sleep(60)
			self._request(ticker, coin)


	def send_msg(self, ticker, price, prev_price, timestamp, up):
		"""
		Method that sends a texts notifying of a significant price move
		
		Parameters
		----------
		ticker : str
			Ticker symbol
		price : float
			Price of ticker
		prev_price : float
			Previous price of ticker
		timestamp : datetime 
			difference in time
		up : bool
			Whether or not the price went up
		"""
		str_price = str(price)
		str_prev_price = str(prev_price)
		if up:
			up = "up"
		else:
			up = "down"
		if timestamp > 60:
			hours = "hours"
			timestamp /= 60
		else:
			hours = "minute"
			if int(hours) != 1:
				hours += "s"
		if ticker == 'SHIB':
			str_price = "{:.8f}".format(price)
			str_prev_price = "{:.8f}".format(prev_price)
		if price > 1:
			str_price = str(round(price, 2))
			str_prev_price = str(round(prev_price, 2))
		content = f'{ticker.upper()} is {up} from ${str_prev_price} to ${str_price} ({round(float((price-prev_price)/prev_price) * 100, 2)}%) in the past {timestamp} {hours}'
		print(f'|{datetime.now()}| {content}')
		self._send_all(reciever, content)


	def _send(self, reciever, content):
		"""Method that sends a message to a reciever with given content"""
		message = client.messages.create(
			body=content,
			from_=MYNUMBER,
			to=reciever)


	def _send_all(self, recievers, content):
		"""Method that sends message to all recievers"""
		for reciever in recievers:
			self._send(reciever, content)


if __name__ == '__main__':
	alerts = Alerts()
