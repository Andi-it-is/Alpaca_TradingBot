from alpaca.trading.requests import* # MarketOrderRequest, OrderRequest
from alpaca.trading.enums import* # OrderSide, TimeInForce


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


