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



#Funktionen


def json_create(ticker: str, period: str):

    """_summary_

    Args:
        ticker (str): Aktien Kürzel; erlaubte Werte sind      AAPL, TSLA, MSFT, NVDA, META, GOOGL
        period (str): Zeiträume die Werte für Aktien beinhaltet; "1y" für 200DMA , "3mo" für 50DMA

    Returns:
        json: Entsprechende erstellte json der jeweiligen Aktie mit dem jeweiligen ticker e.g. GOOGL_50DMA.json
    """


    if period == "1y":
        stock_daten = yf.download(ticker, period="1y")
        stock_DMA_daten = stock_daten['Close'].rolling(window=200).mean()

    elif period == "3mo":
        stock_daten = yf.download(ticker, period="3mo")
        stock_DMA_daten = stock_daten['Close'].rolling(window=50).mean()
    else:
        Exception

    stock_DMA_daten.index = stock_DMA_daten.index.strftime('%Y-%m-%d')
    DMA = stock_DMA_daten.to_dict()
    
    if period == "1y":
        with open(ticker + '_200DMA.json', 'w') as file:                                               #json erstellen
            file.write(json.dumps(DMA, indent=4, sort_keys=True, default=str))
    else:
        with open(ticker + '_50DMA.json', 'w') as file:                                               #json erstellen
            file.write(json.dumps(DMA, indent=4, sort_keys=True, default=str))



    return DMA


def df_create(ticker: str , json50DMA : json, json200DMA : json):

    """die 2 übergebenen jsons sollten von der selben Aktie sein
    technisch ist es möglich ein df von e.g. apple_50DMA und nvidia_200DMA zu erstellen, jedoch ist das Nonsense.
    Lässt man alles über check_signals() erstellen, dann geht das jedoch nicht.

    Args:
        json50DMA (json): json50DMA deiner Aktie,   vorher mit json_create() erstellen
        json200DMA (json): json200DMA deiner Aktie  vorher mit json_create() erstellen

    Returns:
        df (dataframe): erstelltes Dataframe mit 3 Spalten; gemeinsames Datum, Werte für 50DMA, Werte für 200DMA 
    """

    #NaN rausfiltern
    json50DMA = {date: value for date, value in json50DMA.items() if not pd.isna(value)}
    json200DMA = {date: value for date, value in json200DMA.items() if not pd.isna(value)}

    common_dates = sorted(set(json50DMA.keys()).intersection(set(json200DMA.keys())))

    new_df = pd.DataFrame({
        'stock_name' : ticker,
        'common_dates': common_dates,
        '50DMA': [json50DMA[date] for date in common_dates],
        '200DMA': [json200DMA[date] for date in common_dates]
})

    return new_df


def df_update(df):                              #Argument ist das entsprechende df was geupdatet werden soll
    """_summary_

    Args:
        df (dataframe): Input dataframe welches um den Reiter "Signal" erweitert werden soll. In der Funktion check_stock() bzw run_script() wird dieses df erstellt

    Returns:
        df (dataframe): erweitertes dataframe mit den Reitern Signal und dessen Values Buy,Hold,Sell  
    """

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
    return df

