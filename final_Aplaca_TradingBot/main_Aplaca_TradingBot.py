#Imports
from localconfig import config          #config Datei im Projekt  mit api key, secret key, paper url  (wird nicht mit gepusht)
from Daten import*                      #Datei zum Ablagern von Funktionen
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import* 
from alpaca.trading.enums import*
from alpaca.data.requests import*
import time

#Api Instanz erstellen
trading_client = TradingClient(config['API_KEY'], config['SECRET_KEY'], paper=True)
api = tradeapi.REST(config['API_KEY'], config['SECRET_KEY'], config['paper_url'])

#Aktuelle Accountinformationen einholen
account = trading_client.get_account()
for property_name, value in account:
  print(f"\"{property_name}\": {value}")



def check_stock(ticker : str):

  """ Funktion, welche die oben genannte Aktie 'überprüft'
  Zuerst werden Daten gesammelt, formatiert, ausgefiltert und zusammengefügt
  Danach wird der Reiter 'Signal' erstellt, für jedes Datum wird eine Kaufentscheidung beurteilt und diese
  wird hinzugefügt in das Dataframe
   
  Args:
      ticker (str): Erlaubte Aktienkürzel: 
  Returns:
      Aussage (str): Information, dass Aktie analysiert wurde
      df (Dataframe): siehe df_update()
   """
  
    
  # #df muss neu generiert + neu updatet werden bzw die jsons müssen alle 24h neu erstellt werden, um mit """aktuellen""" Daten zu traden
  var1 = json_create(ticker,"3mo")
  var2 = json_create(ticker,"1y")
  old_df = df_create(ticker, var1, var2)
  df = df_update(old_df)


  # Kontrolliert ob 'Buy' in der Spalte Signal ist und ob es der letzte Eintrag(und somit der aktuellste) ist
  if 'Buy' in df['Signal'] and 'Buy' in df.iloc[len(df)-1]:     #im Prinzip doppelt gemoppelt, denn wenn das 2. stimmt, stimmt auch das erste
      
      if df['stock_name'] == 'AAPL':
        print('10x apple gekauft')
        trading_client.submit_order(order_apple_buy)

      elif df['stock_name'] == 'TSLA':
        print('10x tesla gekauft')
        trading_client.submit_order(order_tesla_buy)

      elif df['stock_name'] == 'MSFT':
        print('10x MSFT gekauft')
        trading_client.submit_order(order_microsoft_buy) 

      elif df['stock_name'] == 'NVDA':
        print('10x NVDA gekauft')
        trading_client.submit_order(order_nvidia_buy)

      elif df['stock_name'] == 'META':
        print('10x META gekauft')
        trading_client.submit_order(order_meta_buy)

      elif df['stock_name'] == 'GOOGL':
        print('10x GOOGL gekauft')
        trading_client.submit_order(order_google_buy)



  # Kontrolliert ob 'Sell' in der Spalte Signal ist und ob es der letzte Eintrag(und somit der aktuellste) ist
  if 'Sell' in df['Signal'] and 'Sell' in df.iloc[len(df)-1]:
      
      if df['stock_name'] == 'AAPL':
        print('10x apple verkauft')
        trading_client.submit_order(order_apple_sell)

      elif df['stock_name'] == 'TSLA':
        print('10x tesla verkauft')
        trading_client.submit_order(order_tesla_sell)

      elif df['stock_name'] == 'MSFT':
        print('10x MSFT verkauft')
        trading_client.submit_order(order_microsoft_sell) 

      elif df['stock_name'] == 'NVDA':
        print('10x NVDA verkauft')
        trading_client.submit_order(order_nvidia_sell)

      elif df['stock_name'] == 'META':
        print('10x META verkauft')
        trading_client.submit_order(order_meta_sell)

      elif df['stock_name'] == 'GOOGL':
        print('10x GOOGL verkauft')
        trading_client.submit_order(order_google_sell)

  return(ticker + " wurde analysiert")


def run_script():
  """ Hauptfunktion um Tradingbot zu starten
  """
   
  while True:
    
    check_stock('AAPL')
    check_stock('TSLA')
    check_stock('MSFT')
    check_stock('NVDA')
    check_stock('META')
    check_stock('GOOGL')

    # Abfrage wieder in 24 Stunden, sobald ein neuer Börsentag ist und sich DMA Datenlage aktualisiert 
    time.sleep(24 * 60 * 60)





### Starter ###
run_script()


