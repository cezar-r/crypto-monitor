import time
from datetime import datetime
from twilio.rest import Client
from crypto import Crypto

MYNUMBER = '+18706212431'
account_sid = 'ACe48f94e900c18892f7148d549cae1f5c'
auth_token = '9082f5c18f083ce1b1b673161baeece4'
'''RECOVERY CODE 6KO5wLUndNMbE-jNKOS55CeuIDeeKbFgqBM3uact'''
client = Client(account_sid, auth_token)

CRYPTOS = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT', 'LINK', 'COTI', 'LTC', 'SHIB', 'ALGO']

reciever = ['+16233377431', '+17606684991']
delay = 60 # seconds


class Alerts:

	def __init__(self):
		self.coins = {}
		for ticker in CRYPTOS:
			coin = Crypto(ticker)
			self.coins[ticker] = coin
		# self._send_all(reciever, 'Crypto alerts in bound')
		self.run()

	def run(self):
		while True:
			for ticker, coin in list(self.coins.items()):
				self._request(ticker, coin)
			print(datetime.now())
			time.sleep(delay)


	def _request(self, ticker, coin):
		try:
			price, prev_price, timestamp, up = coin.check()
			if price:
				send_msg(ticker, price, prev_price, timestamp, up)
		except Exception as e:
			print(f'|{datetime.now()}|Exception: {str(e)}, sleeping 60 sec |{ticker} ')
			time.sleep(60)
			self._request(ticker, coin)


	def send_msg(self, ticker, price, prev_privce, timestamp, up):
		if up:
			up = "up"
		else:
			up = "down"
		if timestamp > 60:
			hours = "hours"
			timestamp /= 60
		else:
			hours = "minute"
			if hours != 1:
				hours += "s"
		content = f'{ticker.upper()} is {up} from {prev_price} to {price} ({float(price/prev_price) * 100}%) in the past {timestamp} {hours}'
		print(f'|{time.ctime()}| {content}')
		self._send_all(reciever, content)


	def _send(self, reciever, content):
		message = client.messages.create(
			body=content,
			from_=MYNUMBER,
			to=reciever)


	def _send_all(self, recievers, content):
		for reciever in recievers:
			self._send(reciever, content)


if __name__ == '__main__':
	alerts = Alerts()


