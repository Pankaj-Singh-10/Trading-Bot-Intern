import argparse
import sys
from .validators import *
from .orders import OrderManager
from .client import BinanceClient
from .logging_config import log


def main():
    """Main CLI function to parse arguments and execute orders."""

    # --- Setup Argument Parser ---
    parser = argparse.ArgumentParser(
        description="Simple Trading Bot for Binance Futures Testnet.",
        epilog="Example: python -m bot.cli BTCUSDT BUY MARKET 0.001"
    )

    # Define required arguments
    parser.add_argument(
        "symbol",
        type=str,
        help="Trading pair symbol (e.g., BTCUSDT)"
    )
    parser.add_argument(
        "side",
        type=str,
        choices=['BUY', 'SELL'],
        help="Order side: BUY or SELL"
    )
    parser.add_argument(
        "order_type",
        type=str,
        choices=['MARKET', 'LIMIT'],
        help="Order type: MARKET or LIMIT"
    )
    parser.add_argument(
        "quantity",
        type=str,
        help="Quantity to buy/sell (will be validated)"
    )
    parser.add_argument(
        "price",
        type=str,
        nargs='?',
        default=None,
        help="Required only for LIMIT orders."
    )

    # --- Parse Arguments ---
    args = parser.parse_args()

    # --- 1. Validate Inputs ---
    log.info("--- Order Request Summary ---")
    log.info(f"Symbol: {args.symbol}")
    log.info(f"Side: {args.side}")
    log.info(f"Type: {args.order_type}")
    log.info(f"Quantity: {args.quantity}")
    if args.price:
        log.info(f"Price: {args.price}")
    log.info("-----------------------------")

    if not validate_symbol(args.symbol):
        sys.exit(1)
    if not validate_quantity(args.quantity):
        sys.exit(1)

    qty = float(args.quantity)

    # Price validation for LIMIT orders
    if args.order_type.upper() == 'LIMIT':
        if args.price is None:
            log.error("Price is required for LIMIT orders.")
            sys.exit(1)
        if not validate_price(args.price):
            sys.exit(1)
        price = float(args.price)
    else:
        price = None

    # --- 2. Initialize Client and Order Manager ---
    try:
        binance_client = BinanceClient()
        if not binance_client.test_connection():
            log.error("Could not connect to Binance Testnet. Exiting.")
            sys.exit(1)
        order_manager = OrderManager(binance_client)
    except ValueError as e:
        log.error(f"Initialization failed: {e}")
        sys.exit(1)
    except Exception as e:
        log.error(f"An unexpected error occurred during setup: {e}")
        sys.exit(1)

    # --- 3. Place Order ---
    response = None
    if args.order_type.upper() == 'MARKET':
        response = order_manager.place_market_order(args.symbol, args.side, qty)
    elif args.order_type.upper() == 'LIMIT':
        response = order_manager.place_limit_order(args.symbol, args.side, qty, price)

    # --- 4. Print Output ---
    log.info("--- Order Response Details ---")
    if response and "error" not in response:
        log.info(f"Order ID: {response.get('orderId', 'N/A')}")
        log.info(f"Status: {response.get('status', 'N/A')}")
        log.info(f"Executed Quantity: {response.get('executedQty', 'N/A')}")
        log.info(f"Average Price: {response.get('avgPrice', 'N/A')}")
        log.info("Status: SUCCESS")
    elif response and "error" in response:
        log.error(f"Order Failed. Error: {response['error']}")
    else:
        log.error("No response received from exchange.")
    log.info("-------------------------------")


if __name__ == "__main__":
    main()


