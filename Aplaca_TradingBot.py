# Importing the API and instantiating the REST client according to our keys
import json
import pprint
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = "<oooooooooooooooooooooo>"
SECRET_KEY = "<eeeeeeeeeeeeeeeeeeee>"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Getting account information and printing it
account = trading_client.get_account()
for property_name, value in account:
  print(f"\"{property_name}\": {value}")

# Versuch line 16 in json darzustellen. Klappt irgendwie nicht
# with open(property_name, 'w') as file:
#   json.dump(property_name, file, indent=4)

# Setting parameters for our buy order
market_order_data = MarketOrderRequest(
                      symbol="AAPL",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY             #Zeitupunkt/Methode  der Ausführung der Order?
                  )


#Submitting the order and then printing the returned object
market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
  print(f"\"{property_name}\": {value}")

