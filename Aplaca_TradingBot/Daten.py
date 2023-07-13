from alpaca.trading.requests import* # MarketOrderRequest, OrderRequest
from alpaca.trading.enums import* # OrderSide, TimeInForce
import json
import pandas as pd
import numpy as np
import yfinance as yf

#Alle 6 BUY Orders als Variable für unsere betrachteten Aktien, standardisiert auf .DAY Order und 10 Stück

order_apple_buy = MarketOrderRequest(
                      symbol="AAPL",
                      qty=10,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )

order_tesla_buy = MarketOrderRequest(
                      symbol="TSLA",
                      qty=10,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )

order_microsoft_buy = MarketOrderRequest(
                      symbol="MSFT",
                      qty=10,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )

order_nvidia_buy = MarketOrderRequest(
                      symbol="NVDA",
                      qty=10,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )

order_meta_buy = MarketOrderRequest(
                      symbol="META",
                      qty=10,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )

order_google_buy = MarketOrderRequest(
                      symbol="GOOGL",
                      qty=10,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY                     
                  )



##################################################

#Alle 6 SELL Orders als Variable für unsere betrachteten Aktien, standardisiert auf .DAY Order und 10 Stück

order_apple_sell = MarketOrderRequest(
                      symbol="AAPL",
                      qty=10,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

order_tesla_sell = MarketOrderRequest(
                      symbol="TSLA",
                      qty=10,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

order_microsoft_sell = MarketOrderRequest(
                      symbol="MSFT",
                      qty=10,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

order_nvidia_sell = MarketOrderRequest(
                      symbol="NVDA",
                      qty=10,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

order_meta_sell = MarketOrderRequest(
                      symbol="META",
                      qty=10,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

order_google_sell = MarketOrderRequest(
                      symbol="GOOGL",
                      qty=10,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.DAY                     
                  )

############################# Erstellen von "richtigen" JSON aller 6 Aktien ###############


#def df_create(stock: str):         Den Mammut code hier in eine Funktion packen

#Implementierung vom 200DMA von apple
ticker = 'AAPl'
data = yf.download(ticker, period= "1y")  # Letzten 12 Monate anschauen
data_200DMA = data['Close'].rolling(window=200).mean()  # Arithmetisches Mittel von den letzten 50 close daten bilden
data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') #ins Datetime format bringen
moving_averages_200DMA = data_200DMA.to_dict() # in Dict umwandeln

with open('apple_200DMA.json', 'w') as file:                                               #json erstellen
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))

#Implentierung von 50 DMA von apple
data = yf.download(ticker, period= "3mo")  # Letzten 3 Monate anschauen
data_50DMA = data['Close'].rolling(window=50).mean()  # Arithmetisches Mittel von den letzten 50 close daten bilden
data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d') #ins Datetime format bringen
moving_averages_50DMA = data_50DMA.to_dict() # in Dict umwandeln

with open('apple_50DMA.json', 'w') as file:                                               #json erstellen
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))
#####################################################################

#Implementierung vom 200DMA von tesla
ticker = 'TSLA'
data = yf.download(ticker, period= "1y") 
data_200DMA = data['Close'].rolling(window=200).mean()
data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') 
moving_averages_200DMA = data_200DMA.to_dict()

with open('tesla_200DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))

#Implentierung von 50 DMA von tesla
data = yf.download(ticker, period= "3mo")
data_50DMA = data['Close'].rolling(window=50).mean()
data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d')
moving_averages_50DMA = data_50DMA.to_dict()

with open('tesla_50DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))
#####################################################################

#Implementierung vom 200DMA von microsoft
ticker = 'MSFT'
data = yf.download(ticker, period= "1y") 
data_200DMA = data['Close'].rolling(window=200).mean()
data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') 
moving_averages_200DMA = data_200DMA.to_dict()

with open('microsoft_200DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))

#Implentierung von 50 DMA von microsoft
data = yf.download(ticker, period= "3mo")
data_50DMA = data['Close'].rolling(window=50).mean()
data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d')
moving_averages_50DMA = data_50DMA.to_dict()

with open('microsoft_50DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))
#####################################################################

#Implementierung vom 200DMA von nvidia
ticker = 'NVDA'
data = yf.download(ticker, period= "1y") 
data_200DMA = data['Close'].rolling(window=200).mean()
data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') 
moving_averages_200DMA = data_200DMA.to_dict()

with open('nvidia_200DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))

#Implentierung von 50 DMA von microsoft
data = yf.download(ticker, period= "3mo")
data_50DMA = data['Close'].rolling(window=50).mean()
data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d')
moving_averages_50DMA = data_50DMA.to_dict()

with open('nvidia_50DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))
#####################################################################

#Implementierung vom 200DMA von meta
ticker = 'META'
data = yf.download(ticker, period= "1y") 
data_200DMA = data['Close'].rolling(window=200).mean()
data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') 
moving_averages_200DMA = data_200DMA.to_dict()

with open('meta_200DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))

#Implentierung von 50 DMA von microsoft
data = yf.download(ticker, period= "3mo")
data_50DMA = data['Close'].rolling(window=50).mean()
data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d')
moving_averages_50DMA = data_50DMA.to_dict()

with open('meta_50DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))
#####################################################################

#Implementierung vom 200DMA von google
ticker = 'GOOGL'
data = yf.download(ticker, period= "1y") 
data_200DMA = data['Close'].rolling(window=200).mean()
data_200DMA.index = data_200DMA.index.strftime('%Y-%m-%d') 
moving_averages_200DMA = data_200DMA.to_dict()

with open('google_200DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_200DMA, indent=4, sort_keys=True, default=str))

#Implentierung von 50 DMA von microsoft
data = yf.download(ticker, period= "3mo")
data_50DMA = data['Close'].rolling(window=50).mean()
data_50DMA.index = data_50DMA.index.strftime('%Y-%m-%d')
moving_averages_50DMA = data_50DMA.to_dict()

with open('google_50DMA.json', 'w') as file:
    file.write(json.dumps(moving_averages_50DMA, indent=4, sort_keys=True, default=str))
#####################################################################

##########################################################################################





############################# Alle 6 Aktien als Dataframe ############



#jsons öffnen, damit Daten.py diese einliest
with open('apple_50DMA.json', 'r') as file:
    data_50DMA = json.load(file)

with open('apple_200DMA.json', 'r') as file:
    data_200DMA = json.load(file)

# NaN Werte rausfiltern
data_50DMA = {date: value for date, value in data_50DMA.items() if not pd.isna(value)}
data_200DMA = {date: value for date, value in data_200DMA.items() if not pd.isna(value)}

# Gemeinsame Datums filtern
common_dates = sorted(set(data_50DMA.keys()).intersection(set(data_200DMA.keys())))

apple_df = pd.DataFrame({
    'common_dates': common_dates,
    '50DMA': [data_50DMA[date] for date in common_dates],
    '200DMA': [data_200DMA[date] for date in common_dates]
})

print('--- Apple Daten ---')
print(apple_df)
print('-------------------')
################################################################

with open('tesla_50DMA.json', 'r') as file:
    data_50DMA = json.load(file)

with open('tesla_200DMA.json', 'r') as file:
    data_200DMA = json.load(file)

data_50DMA = {date: value for date, value in data_50DMA.items() if not pd.isna(value)}
data_200DMA = {date: value for date, value in data_200DMA.items() if not pd.isna(value)}

common_dates = sorted(set(data_50DMA.keys()).intersection(set(data_200DMA.keys())))

tesla_df = pd.DataFrame({
    'common_dates': common_dates,
    '50DMA': [data_50DMA[date] for date in common_dates],
    '200DMA': [data_200DMA[date] for date in common_dates]
})

print('--- Tesla Daten ---')
print(tesla_df)
print('-------------------')
################################################################

with open('microsoft_50DMA.json', 'r') as file:
    data_50DMA = json.load(file)

with open('microsoft_200DMA.json', 'r') as file:
    data_200DMA = json.load(file)

data_50DMA = {date: value for date, value in data_50DMA.items() if not pd.isna(value)}
data_200DMA = {date: value for date, value in data_200DMA.items() if not pd.isna(value)}

common_dates = sorted(set(data_50DMA.keys()).intersection(set(data_200DMA.keys())))

microsoft_df = pd.DataFrame({
    'common_dates': common_dates,
    '50DMA': [data_50DMA[date] for date in common_dates],
    '200DMA': [data_200DMA[date] for date in common_dates]
})

print('--- Microsoft Daten ---')
print(microsoft_df)
print('-------------------')
################################################################

with open('nvidia_50DMA.json', 'r') as file:
    data_50DMA = json.load(file)

with open('nvidia_200DMA.json', 'r') as file:
    data_200DMA = json.load(file)

data_50DMA = {date: value for date, value in data_50DMA.items() if not pd.isna(value)}
data_200DMA = {date: value for date, value in data_200DMA.items() if not pd.isna(value)}

common_dates = sorted(set(data_50DMA.keys()).intersection(set(data_200DMA.keys())))

nvidia_df = pd.DataFrame({
    'common_dates': common_dates,
    '50DMA': [data_50DMA[date] for date in common_dates],
    '200DMA': [data_200DMA[date] for date in common_dates]
})

print('--- Nvidia Daten ---')
print(nvidia_df)
print('-------------------')
################################################################

with open('meta_50DMA.json', 'r') as file:
    data_50DMA = json.load(file)

with open('meta_200DMA.json', 'r') as file:
    data_200DMA = json.load(file)

data_50DMA = {date: value for date, value in data_50DMA.items() if not pd.isna(value)}
data_200DMA = {date: value for date, value in data_200DMA.items() if not pd.isna(value)}

common_dates = sorted(set(data_50DMA.keys()).intersection(set(data_200DMA.keys())))

meta_df = pd.DataFrame({
    'common_dates': common_dates,
    '50DMA': [data_50DMA[date] for date in common_dates],
    '200DMA': [data_200DMA[date] for date in common_dates]
})

print('--- Meta Daten ---')
print(meta_df)
print('-------------------')
################################################################

with open('google_50DMA.json', 'r') as file:
    data_50DMA = json.load(file)

with open('google_200DMA.json', 'r') as file:
    data_200DMA = json.load(file)

data_50DMA = {date: value for date, value in data_50DMA.items() if not pd.isna(value)}
data_200DMA = {date: value for date, value in data_200DMA.items() if not pd.isna(value)}

common_dates = sorted(set(data_50DMA.keys()).intersection(set(data_200DMA.keys())))

google_df = pd.DataFrame({
    'common_dates': common_dates,
    '50DMA': [data_50DMA[date] for date in common_dates],
    '200DMA': [data_200DMA[date] for date in common_dates]
})

print('--- Google Daten ---')
print(google_df)
print('-------------------')
################################################################


##########################################################################################






# Funktionen #



def df_update(df):                              #Argument ist das entsprechende df was geupdatet werden soll wie z.B. apple_df
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

    


