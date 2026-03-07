import re
from .logging_config import log

def validate_symbol(symbol: str) -> bool:
    """Check if the symbol is in a valid format (e.g., BTCUSDT)."""
    if not re.match(r"^[A-Z0-9]+USDT$", symbol.upper()):
        log.warning(f"Validation failed: Symbol '{symbol}' is not valid. It should end with USDT (e.g., BTCUSDT).")
        return False
    return True

def validate_quantity(quantity: str) -> bool:
    """Check if quantity is a positive number."""
    try:
        qty = float(quantity)
        if qty <= 0:
            log.warning("Validation failed: Quantity must be positive.")
            return False
        return True
    except ValueError:
        log.warning("Validation failed: Quantity must be a number.")
        return False

def validate_price(price: str) -> bool:
    """Check if price is a positive number."""
    try:
        prc = float(price)
        if prc <= 0:
            log.warning("Validation failed: Price must be positive.")
            return False
        return True
    except ValueError:
        log.warning("Validation failed: Price must be a number.")
        return False

def validate_side(side: str) -> bool:
    """Check if side is BUY or SELL."""
    return side.upper() in ["BUY", "SELL"]

def validate_order_type(order_type: str) -> bool:
    """Check if order type is MARKET or LIMIT."""
    return order_type.upper() in ["MARKET", "LIMIT"]


