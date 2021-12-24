# crypto-monitor

### Background
Crypto is one of the fastest growing "things" of all time. It is currently outpacing other technologies, such as the Internet, in terms of adoption. It is also outpacing every asset class, such as gold, in terms of price. Everyday, more and more people buy their first cryptocurrency, whether it be Bitcoin, Ethereum, or any of the 2000+ listed cryptocurrencies. Cryptocurrencies are also known for having a very volatile market, with some tokens moving +/- 5% in a matter of minutes. Because of this, I made this crypto monitor, which will send a text every time there is a move >= 5% on a variety of cryptos.

## Getting Live Price Data
To get live price updates, I utilized the [KuCoin API](https://docs.kucoin.com/). The code for this can be found in [KuCoinAPI.py](https://github.com/cezar-r/crypto-monitor/blob/main/src/KuCoinAPI.py).

## Checking Price Differences
Each crypto is stored as its own object during runtime. One of the attributes of this crypto object is the prices dictionary. This is where the price data and timestamp are stored, with the timestamp being the key. Every minute, a check() funciton is ran that gets the current price of the crypto, then iterates over the dictionary of prices and looks for a >5% difference in price. If there is one, the current price, original price, and timestamp difference are returned, as well as the prices dictionary being cleared to avoid overlapping pings.

## Sending Messages
Once a change in price has occurred a text needs to be sent. To do this, I utilized [Twilio](https://www.twilio.com/docs/usage/api), which made it very simple to send out text messages.

## TODO
My main goal with this program is to convert it to a web application that anyone can use. This website would allow you to make an account, and then store which cryptos you want to get notified for, as well what price difference threshold. 

## Technologies Used
 - KuCoin API
 - Twilio
