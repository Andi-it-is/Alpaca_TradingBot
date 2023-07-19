import alpaca_trade_api as tradeapi
import time

# Alpaca API-Zugangsdaten
API_KEY = 'xxx'
API_SECRET = 'xx'
BASE_URL = 'https://paper-api.alpaca.markets' 


# Alpaca API-Verbindung herstellen
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

# Strategie-Klasse
class SwingHighStrategy:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = []
        self.order_number = 0

    def get_last_price(self):
        bar = api.get_barset(self.symbol, 'minute', limit=1)[self.symbol][0]
        return bar.c

    def create_order(self, quantity, side):
        return {
            'symbol': self.symbol,
            'qty': quantity,
            'side': side,
            'type': 'market',
            'time_in_force': 'gtc'
        }

    def submit_order(self, order):
        api.submit_order(
            symbol=order['symbol'],
            qty=order['qty'],
            side=order['side'],
            type=order['type'],
            time_in_force=order['time_in_force']
        )

    def sell_all(self):
        position = api.get_position(self.symbol)
        if position:
            quantity = int(position.qty)
            order = self.create_order(quantity, 'sell')
            self.submit_order(order)

    def run_strategy(self):
        while True:
            entry_price = self.get_last_price()
            print(f"Position: {api.get_position(self.symbol)}")
            self.data.append(entry_price)

            if len(self.data) > 3:
                temp = self.data[-3:]
                if temp[-1] > temp[1] > temp[0]:
                    print(f"Last 3 prints: {temp}")
                    order = self.create_order(10, 'buy')
                    self.submit_order(order)
                    self.order_number += 1
                    if self.order_number == 1:
                        print(f"Entry price: {temp[-1]}")
                        entry_price = temp[-1]  # filled price
                if api.get_position(self.symbol) and entry_price * 0.995 > entry_price:
                    self.sell_all()
                    self.order_number = 0
                elif api.get_position(self.symbol) and entry_price * 1.015 <= entry_price:
                    self.sell_all()
                    self.order_number = 0

            time.sleep(60)  # 60 Sekunden warten zwischen den Iterationen

    def before_market_closes(self):
        self.sell_all()

# Hauptfunktion
def main():
    symbol = "GOOG"
    strategy = SwingHighStrategy(symbol)
    strategy.run_strategy()


    main()
    print("kot")

