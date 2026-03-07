from binance.exceptions import BinanceAPIException
from .client import BinanceClient
from .logging_config import log


class OrderManager:
    """Handles order placement logic for Spot Testnet."""

    def __init__(self, client: BinanceClient):
        self.client = client

    def place_market_order(self, symbol: str, side: str, quantity: float):
        """Place a market order on Spot Testnet."""
        log.info(f"Attempting to place MARKET order: {side} {quantity} {symbol}")
        try:
            # For Spot Testnet, use the appropriate methods
            if side.upper() == 'BUY':
                order = self.client.client.order_market_buy(
                    symbol=symbol.upper(),
                    quantity=quantity
                )
            else:  # SELL
                order = self.client.client.order_market_sell(
                    symbol=symbol.upper(),
                    quantity=quantity
                )

            log.info(f"Market order placed successfully. Order ID: {order['orderId']}")
            return order
        except BinanceAPIException as e:
            log.error(f"Binance API error placing market order: {e}")
            return {"error": f"API Error: {e.message}"}
        except Exception as e:
            log.error(f"Unexpected error placing market order: {e}")
            return {"error": f"Unexpected Error: {str(e)}"}

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        """Place a limit order on Spot Testnet."""
        log.info(f"Attempting to place LIMIT order: {side} {quantity} {symbol} at {price}")
        try:
            if side.upper() == 'BUY':
                order = self.client.client.order_limit_buy(
                    symbol=symbol.upper(),
                    quantity=quantity,
                    price=str(price)
                )
            else:  # SELL
                order = self.client.client.order_limit_sell(
                    symbol=symbol.upper(),
                    quantity=quantity,
                    price=str(price)
                )

            log.info(f"Limit order placed successfully. Order ID: {order['orderId']}")
            return order
        except BinanceAPIException as e:
            log.error(f"Binance API error placing limit order: {e}")
            return {"error": f"API Error: {e.message}"}
        except Exception as e:
            log.error(f"Unexpected error placing limit order: {e}")
            return {"error": f"Unexpected Error: {str(e)}"}