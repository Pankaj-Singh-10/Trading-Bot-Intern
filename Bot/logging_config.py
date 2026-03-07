import logging
import sys
from pathlib import Path

# Create a 'logs' directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)


def setup_logging():
    """Configures logging for the application."""

    # Create a custom logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    # Prevent adding multiple handlers if the function is called again
    if logger.handlers:
        return logger

    # --- Create Handlers ---
    # 1. Console Handler: For output to the terminal
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # 2. File Handler: For saving all logs to a file
    file_handler = logging.FileHandler(log_dir / "bot_activity.log")
    file_handler.setLevel(logging.DEBUG)

    # --- Create Formatters ---
    # Formatter for console: Simple and clean
    console_format = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_format)

    # Formatter for file: Detailed with timestamp
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    # --- Add handlers to the logger ---
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Create a global logger instance
log = setup_logging()


