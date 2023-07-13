# Importing the API and instantiating the REST client according to our keys
from localconfig import config    #config Datei im Projekt  mit api key, secret key, paper url  (wird nicht mit gepusht)
from Daten import*   #andere Datei wo Order instanzen erstellt werden. diese gilt es dann auszuführen
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import* # MarketOrderRequest, OrderRequest
from alpaca.trading.enums import* # OrderSide, TimeInForce
from alpaca.data.requests import*
import yfinance as yf
import pandas as pd
import numpy as np
import json
from alpaca.data.live import*
import time


trading_client = TradingClient(config['API_KEY'], config['SECRET_KEY'], paper=True)
api = tradeapi.REST(config['API_KEY'], config['SECRET_KEY'], config['paper_url'])



# Getting account information and printing it
account = trading_client.get_account()
for property_name, value in account:
  print("test")
  #print(f"\"{property_name}\": {value}")



# #Submitting order 
# #market_order = trading_client.submit_order(order_google_buy)

# # and then printing the returned object
# for property_name, value in market_order:
#   print(f"\"{property_name}\": {value}")


print(apple_df.iloc[len(apple_df)-1])

df_update(apple_df)
df_update(tesla_df)
df_update(microsoft_df)
df_update(nvidia_df)
df_update(meta_df)
df_update(google_df)



def check_signals(df):
    while True:
        #df muss neu generiert + neu updatet werden, oder die jsons müssen alle 24h neu erstellt werden
        #df_create()
        #df_update()


        # Kontrolliert ob 'Buy' in der Spalte Signal ist und ob es der letzte Eintrag(und somit der aktuellste) ist
        if 'Buy' in df['Signal'] and 'Buy' in df.iloc[len(df)-1]:
            if df == apple_df:
              trading_client.submit_order(order_apple_buy)

            elif df == tesla_df:
              trading_client.submit_order(order_tesla_buy)

            elif df == microsoft_df:
              trading_client.submit_order(order_microsoft_buy) 

            elif df == nvidia_df:
              trading_client.submit_order(order_nvidia_buy)

            elif df == meta_df:
              trading_client.submit_order(order_meta_buy)

            elif df == google_df:
              trading_client.submit_order(order_google_buy)

            else:
               continue   


        # Kontrolliert ob 'Sell' in der Spalte Signal ist und ob es der letzte Eintrag(und somit der aktuellste) ist
        if 'Sell' in df['Signal'] and 'Sell' in df.iloc[len(df)-1]:
            if df == apple_df:
              trading_client.submit_order(order_apple_sell)

            elif df == tesla_df:
              trading_client.submit_order(order_tesla_sell)

            elif df == microsoft_df:
              trading_client.submit_order(order_microsoft_sell) 

            elif df == nvidia_df:
              trading_client.submit_order(order_nvidia_sell)

            elif df == meta_df:
              trading_client.submit_order(order_meta_sell)

            elif df == google_df:
              trading_client.submit_order(order_google_sell)

            else:
               continue


        # Abfrage wieder in 24 Stunden, sobald DMA neue Daten hat
        time.sleep(24 * 60 * 60)



check_signals(apple_df)





################### gilt zu testen 
# import time

# def check_signals(df):
#     previous_df = df.copy()  # Make a copy of the DataFrame to compare changes

#     while True:
#         # Check for changes in the DataFrame
#         if not df.equals(previous_df):
#             print("Change detected!")
#             # Perform actions when a change occurs

#             # Update the previous_df to the new DataFrame state
#             previous_df = df.copy()

#         # Delay for a specific time before checking again
#         time.sleep(60)  # Sleep for 60 seconds (adjust as needed)

# # Call df_create() and store the returned DataFrame in a variable
# df = df_create()

# # Call check_signals() function
# check_signals(df)