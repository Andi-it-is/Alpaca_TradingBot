# Importing the API and instantiating the REST client according to our keys
from localconfig import config    #config Datei im Projekt  mit api key, secret key, paper url  (wird nicht mit gepusht)
from Orders_erstellen import*   #andere Datei wo Order instanzen erstellt werden. diese gilt es dann auszuführen
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import* # MarketOrderRequest, OrderRequest
from alpaca.trading.enums import* # OrderSide, TimeInForce
from alpaca.data.requests import*
import yfinance as yf
import pandas as pd
import json
import numpy as np
from alpaca.data.live import*



trading_client = TradingClient(config['API_KEY'], config['SECRET_KEY'], paper=True)
api = tradeapi.REST(config['API_KEY'], config['SECRET_KEY'], config['paper_url'])



# Getting account information and printing it
account = trading_client.get_account()
for property_name, value in account:
  #print(f"\"{property_name}\": {value}")



# #Submitting order 
# #market_order = trading_client.submit_order(order_google_buy)

# # and then printing the returned object
# for property_name, value in market_order:
#   print(f"\"{property_name}\": {value}")



#Implementierung vom 200DMA von apple
    ticker = 'AAPl'

data = yf.download(ticker, period= "1y")  # Letzten 12 Monate anschauen

data_200DMA = data['Close'].rolling(window=200).mean()  # Arithmetisches Mittel von den letzten 50 close daten bilden

data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') #ins Datetime format bringen

moving_averages_200DMA = data_200DMA.to_dict() # in Dict umwandeln

with open('moving_averages_200DMA.json', 'w') as file:                                               #json erstellen
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))




#Implentierung von 50 DMA von apple
data = yf.download(ticker, period= "3mo")  # Letzten 3 Monate anschauen

data_50DMA = data['Close'].rolling(window=50).mean()  # Arithmetisches Mittel von den letzten 50 close daten bilden

data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d') #ins Datetime format bringen

moving_averages_50DMA = data_50DMA.to_dict() # in Dict umwandeln

with open('moving_averages_50DMA.json', 'w') as file:                                               #json erstellen
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))



common_dates = set(moving_averages_50DMA.keys()).intersection(set(moving_averages_200DMA.keys()))

# Extract the values for the common dates, excluding NaN values
value50DMA = [moving_averages_50DMA[date] for date in common_dates if not np.isnan(moving_averages_50DMA[date])]
value200DMA = [moving_averages_200DMA[date] for date in common_dates if not np.isnan(moving_averages_200DMA[date])]
value200DMA = value200DMA[-len(value50DMA):]

print(value50DMA)
print(len(value50DMA))

print(value200DMA)
print(len(value200DMA))




df = pd.DataFrame({'50DMA': value50DMA, '200DMA': value200DMA})

print(df)


# Initialize trading parameters
short_period = 50
long_period = 200
current_status = "neutral"
trading_signals = []

# Iterate through the historical data
for i in range(0, len(df)):
    if df['50DMA'].iloc[i] > df['200DMA'].iloc[i] and current_status == "neutral":
        trading_signals.append("Buy")
        current_status = "long"
    elif df['50DMA'].iloc[i] < df['200DMA'].iloc[i] and current_status == "long":
        trading_signals.append("Sell")
        current_status = "neutral"
    elif df['50DMA'].iloc[i] < df['200DMA'].iloc[i] and current_status == "neutral":
        trading_signals.append("Sell")
        current_status = "short"
    elif df['50DMA'].iloc[i] > df['200DMA'].iloc[i] and current_status == "short":
        trading_signals.append("Buy")
        current_status = "neutral"
    else:
        trading_signals.append("Hold")

# Add the trading signals to the DataFrame
df['Signal'] = trading_signals

print(df)




