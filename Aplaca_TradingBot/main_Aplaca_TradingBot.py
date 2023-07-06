# Importing the API and instantiating the REST client according to our keys
from localconfig import config #config Datei im Projekt  mit api key, secret key, paper url  (wird nicht mit gepusht)
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import* # MarketOrderRequest, OrderRequest
from alpaca.trading.enums import* # OrderSide, TimeInForce
from alpaca.data.requests import*
import yfinance as yf
import pandas as pd
import json


trading_client = TradingClient(config['API_KEY'], config['SECRET_KEY'], paper=True)
api = tradeapi.REST(config['API_KEY'], config['SECRET_KEY'], config['paper_url'])

# Getting account information and printing it
# account = trading_client.get_account()
# for property_name, value in account:
#   print(f"\"{property_name}\": {value}")


# Setting parameters for Buy order
market_order_data = MarketOrderRequest(
                      symbol="NVDA",
                      qty=13,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )


#Submitting the order and then printing the returned object
market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
  print(f"\"{property_name}\": {value}")



# Setting parameters for Sell order
market_order_data = MarketOrderRequest(
                      symbol="MSFT",
                      qty=30,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
  print(f"\"{property_name}\": {value}")






#######################################


ticker = "AAPL"  # Ticker symbol for Apple
data = yf.download(ticker, period="1y")  # Retrieve 1 year of data
data['200DMA'] = data['Close'].rolling(window=200).mean()

# Convert the timestamps to string format
data.index = data.index.strftime('%Y-%m-%d')

# Select only the '200DMA' column and convert it to a dictionary
moving_averages = data[['200DMA']].to_dict(orient='index')

# Save the moving averages as a JSON file
with open('moving_averages.json', 'w') as file:
    file.write(json.dumps(moving_averages, indent=4, sort_keys=True, default=str))