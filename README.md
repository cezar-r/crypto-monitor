# crypto-monitor

### Background
Crypto is one of the fastest growing "things" of all time. It is currently outpacing other technologies, such as the Internet, in terms of adoption. It is also outpacing every asset class, such as gold, in terms of price. Everyday, more and more people buy their first cryptocurrency, whether it be Bitcoin, Ethereum, or any of the 2000+ listed cryptocurrencies. Cryptocurrencies are also known for having a very volatile market, with some tokens moving +/- 5% in a matter of minutes. Because of this, I made this crypto monitor, which will send a text every time there is a move >= 5% on a variety of cryptos.

## Getting Live Price Data
To get live price updates, I utilized the [KuCoin API](https://docs.kucoin.com/). The code for this can be found in [KuCoinAPI.py](https://github.com/cezar-r/crypto-monitor/blob/main/src/KuCoinAPI.py).

## Checking Price Differences
Each crypto is stored as its own object during runtime. One of the attributes of this crypto object is the prices dictionary. This is where the price data and timestamp are stored, with the timestamp being the key. Every minute, a check() funciton is ran that gets the current price of the crypto, then iterates over the dictionary of prices and looks for a >5% difference in price. If there is one, the current price, original price, and timestamp difference are returned, as well as the prices dictionary being cleared to avoid overlapping pings.

## Sending Messages
Once a change in price has occurred a text needs to be sent. To do this, I utilized [Twilio](https://www.twilio.com/docs/usage/api), which made it very simple to send out text messages.

## In Action
 - Below is an example of the pings you would recieve using the monitor. 
<img src = "https://github.com/cezar-r/crypto-monitor/blob/main/monitor_ss.jpeg" width = 200 height = 380> 

 - I personally use Coinbase and I realized that Coinbase sends "significant price action" notifications much later than when they actually occur, which was one of my main motives for making this monitor. Below you can see the time difference between the monitor and Coinbase's notifications.
<img src = "https://github.com/cezar-r/crypto-monitor/blob/main/monitor_vs_coinbase.jpg" width = 200 height = 350> 

The small group of users that are currently recieving messages have found great utility in this monitor and they claim it has helped them a lot. For example, on December 3rd, the entire crypto market experienced a "flash crash", where prices tanked more than 20% in a matter of minutes and quickly recovered after. Because of the monitor, the group of users were able to take advantage of these low prices (that many people most likely missed out on) and where able to place orders at a much lower price.

## TODO
My main goal with this program is to convert it to a web application that anyone can use. This website would allow you to make an account, and then store which cryptos you want to get notified for, as well what price difference threshold you want to get notified on. 

## Technologies Used
 - KuCoin API
 - Twilio
