from cryptos import Cardano, Bitcoin, Ethereum, Doge
import requests
import json
from datetime import datetime, timedelta
import smtplib
import time


def get_json(coin_str):
	now = datetime.now() + timedelta(hours=7)
	hours = 5 
	hours_added = timedelta(hours = hours)
	end_date = str(now + hours_added)
	end_date = end_date[:-10]
	end_date = end_date.replace(' ', 'T')
	start_date = ''
	date_split = end_date.split('-')
	day_time = date_split[2]
	day = day_time[:-6]
	day = str(int(day) - 1)
	if len(day) == 1:
		day = '0'+ day
	day_time = day + day_time[2:]
	date_split[2] = day_time
	start_date = '-'.join(date_split)
	url = 'https://production.api.coindesk.com/v2/price/values/' + coin_str + '?start_date=' + start_date + '&end_date=' + end_date + '&ohlc=false'
	print(url)
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data


def get_cur_price(json):
	data = json['data']
	entries = data['entries']
	cur_price = entries[-1][1]
	return cur_price


def send_msg(price, crypto):
	content = f'{crypto} is at {price}'
	reciever = '<RECIEVER INFO HERE>'
	my_email = '<EMAIL THAT IS SENDING TEXTS>'
	my_email_pw = '<EMAIL PASSWORD>'

	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login(my_email, my_email_pw)
	mail.sendmail(my_email, reciever, content)

def doge_possible_alert(price, crypto = "Doge"):
	if price < .1 and doge.under_10 == False:
		send_msg(price, crypto)
		doge.under_10 = True
	elif price < .15 and doge.under_15 == False:
		send_msg(price, crypto)
		doge.under_15 = True
	elif price < .2 and doge.under_20 == False:
		send_msg(price, crypto)
		doge.under_20 = True
	elif price < .25 and doge.under_25 == False:
		send_msg(price, crypto)
		doge.under_25 = True
	elif price < .3 and doge.under_30 == False:
		send_msg(price, crypto)
		doge.under_30 = True
	return


def ada_possible_alert(price, crypto="ADA"):
	if price < 1 and ada.under_1_00 == False:
		send_msg(price, crypto)
		ada.under_1_00 = True
	elif price < 1.1 and ada.under_1_10 == False:
		send_msg(price, crypto)
		ada.under_1_10 = True
	elif price < 1.2 and ada.under_1_20 == False:
		send_msg(price, crypto)
		ada.under_1_20 = True
	elif price < 1.3 and ada.under_1_30 == False:
		send_msg(price, crypto)
		ada.under_1_30 = True
	elif price < 1.4 and ada.under_1_40 == False:
		send_msg(price, crypto)
		ada.under_1_40 = True
	elif price < 1.5 and ada.under_1_50 == False:
		send_msg(price, crypto)
		ada.under_1_50 = True
	elif price < 1.6 and ada.under_1_60 == False:
		send_msg(price, crypto)
		ada.under_1_60 =  True
	return 


def eth_possible_alert(price, crypto="ETH"):
	price = round(price, 2)
	if price < 1500 and eth.under_1_5k == False:
		send_msg(price, crypto)
		eth.under_1_5k = True
	elif price < 1800 and eth.under_1_8k == False:
		send_msg(price, crypto)
		eth.under_1_8k = True
	elif price < 2000 and eth.under_2k == False:
		send_msg(price, crypto)
		eth.under_2k = True
	elif price < 2200 and eth.under_2_2k == False:
		send_msg(price, crypto)
		eth.under_2_2k = True
	elif price < 2500 and eth.under_2_5k == False:
		send_msg(price, crypto)
		eth.under_2_5k = True
	elif price < 2600 and eth.under_2_6k == False:
		send_msg(price, crypto)
		eth.under_2_6k = True
	elif price < 2800 and eth.under_2_8k == False:
		send_msg(price, crypto)
		eth.under_2_8k = True
	elif price < 3000 and eth.under_3k == False:
		send_msg(price, crypto)
		eth.under_3k = True
	return 

def btc_possible_alert(price, crypto="BTC"):
	price = round(price, 2)
	if price < 20000 and btc.under_20k == False:
		send_msg(price, crypto)
		btc.under_20k = True
	elif price < 22000 and btc.under_22k == False:
		send_msg(price, crypto)
		btc.under_22k = True
	elif price < 25000 and btc.under_25k == False:
		send_msg(price, crypto)
		btc.under_25k = True
	elif price < 26000 and btc.under_26k == False:
		send_msg(price, crypto)
		btc.under_26k = True
	elif price < 28000 and btc.under_28k == False:
		send_msg(price, crypto)
		btc.under_28k = True
	elif price < 30000 and btc.under_30k == False:
		send_msg(price, crypto)
		btc.under_30k = True
	elif price < 35000 and btc.under_35k == False:
		send_msg(price, crypto)
		btc.under_35k = True
	return 


def doge_monitor(doge):
	json_data = get_json("DOGE")
	doge.cur_price = get_cur_price(json_data)
	doge_possible_alert(doge.cur_price)


def ada_monitor(ada):
	json_data = get_json("ADA")
	ada.cur_price = get_cur_price(json_data)
	ada_possible_alert(ada.cur_price)


def eth_monitor(eth):
	json_data = get_json("ETH")
	eth.cur_price = get_cur_price(json_data)
	eth_possible_alert(eth.cur_price)


def btc_monitor(btc):
	json_data = get_json("BTC")
	btc.cur_price = get_cur_price(json_data)
	btc_possible_alert(btc.cur_price)

doge = Doge()
ada = Cardano()
eth = Ethereum()
btc = Bitcoin()

btc.init_lvls()
eth.init_lvls()
ada.init_lvls()
doge.init_lvls()

while __name__ == "__main__":
	doge_monitor(doge)
	print(f'{datetime.now()}Doge:{doge.cur_price}')
	ada_monitor(ada)
	print(f'{datetime.now()}Cardano:{ada.cur_price}')
	eth_monitor(eth)
	print(f'{datetime.now()}Ethereum:{eth.cur_price}')
	btc_monitor(btc)
	print(f'{datetime.now()}Bitcoin:{btc.cur_price}')
	btc.init_lvls()
	eth.init_lvls()
	ada.init_lvls()
	doge.init_lvls()
	time.sleep(600)
