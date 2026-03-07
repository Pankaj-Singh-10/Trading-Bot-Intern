from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import os
from .logging_config import log

# Load environment variables from the .env file
load_dotenv()


class BinanceClient:
    """A wrapper for the Binance Spot Testnet client."""

    def __init__(self):
        """Initialize the client with API keys and testnet URL."""
        self.api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        self.api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")

        if not self.api_key or not self.api_secret:
            log.error("API keys not found. Please check your .env file.")
            raise ValueError("API keys missing")

        try:
            # Initialize the client with testnet=True for Spot Testnet
            self.client = Client(self.api_key, self.api_secret, testnet=True)

            # Set the correct Spot Testnet URL
            self.client.API_URL = 'https://testnet.binance.vision/api'

            log.info("Binance Spot Testnet client initialized successfully.")
            log.info(f"Using URL: {self.client.API_URL}")
        except Exception as e:
            log.error(f"Failed to initialize Binance client: {e}")
            raise

    def test_connection(self):
        """Test the connection to the exchange."""
        try:
            # Try to get account info (requires authentication)
            account = self.client.get_account()
            log.info(f"Connection successful! Account has {len(account['balances'])} balances")
            log.info(f"Can trade: {account.get('canTrade', False)}")
            return True
        except BinanceAPIException as e:
            log.error(f"API Error during connection test: {e}")
            return False
        except Exception as e:
            log.error(f"Unexpected error during connection test: {e}")
            return False