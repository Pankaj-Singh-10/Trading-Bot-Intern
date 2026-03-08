# Binance Spot Testnet Trading Bot

A professional Python-based trading bot for Binance Spot Testnet that can place market and limit orders with comprehensive logging, input validation, and error handling.

## 📋 Features

- **Market Orders** - Buy and sell instantly at current market price
- **Limit Orders** - Buy and sell at specified price with GTC (Good-Till-Cancelled)
- **Both Sides** - Support for BUY and SELL orders
- **Input Validation** - Validates symbol format, quantity, price, and order parameters
- **Comprehensive Logging** - Detailed logs for debugging and audit trail
- **Error Handling** - Graceful handling of API errors, network issues, and invalid inputs
- **Clean Architecture** - Separated client, orders, validation, and CLI layers
- **User-Friendly CLI** - Simple command-line interface with clear output

## Project Structure

trading-bot-intern/
├── bot/
│ ├── init.py # Package initializer
│ ├── client.py # Binance API client wrapper
│ ├── cli.py # Command-line interface
│ ├── logging_config.py # Logging configuration
│ ├── orders.py # Order placement logic
│ └── validators.py # Input validation functions
├── logs/ # Order log files
│ ├── market_order.log # Sample market order log
│ └── limit_order.log # Sample limit order log
├── .env # API keys (not committed to GitHub)
├── .gitignore # Git ignore rules
├── README.md # This file
└── requirements.txt # Python dependencies


## Getting Started

### Prerequisites

- Python 3.7 or higher
- Binance Spot Testnet account
- GitHub account (for submission)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pankaj-Singh-10/Trading-Bot-Intern.git
   cd Trading-Bot-Intern

2. **Create and activate virtual environment**

Windows:

python -m venv .venv
.venv\Scripts\activate

Mac/Linux:

python -m venv .venv
source .venv/bin/activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Set up Binance Testnet API Keys**

a. Go to https://testnet.binance.vision/
b. Login with GitHub
c. Navigate to API Management
d. Generate new API key with permissions:
   -Trade
   -User Data
   -User Stream
e. Copy your API Key and Secret Key

5. **Create .env file in the root directory**

BINANCE_TESTNET_API_KEY=your_api_key_here
BINANCE_TESTNET_SECRET_KEY=your_secret_key_here

Never commit this file to GitHub!

## Usage Examples

a. **Place a Market Buy Order**
python -m bot.cli BTCUSDT BUY MARKET 0.001

b. **Place a Market Sell Order**
python -m bot.cli BTCUSDT SELL MARKET 0.001

c. **Place a Limit Buy Order**
python -m bot.cli BTCUSDT BUY LIMIT 0.001 67000

d. **Place a Limit Sell Order**
python -m bot.cli BTCUSDT SELL LIMIT 0.001 68000

## Sample Output

**Market Order Success**

INFO: --- Order Request Summary ---
INFO: Symbol: BTCUSDT
INFO: Side: BUY
INFO: Type: MARKET
INFO: Quantity: 0.001
INFO: -----------------------------
INFO: Binance Spot Testnet client initialized successfully.
INFO: Using URL: https://testnet.binance.vision/api
INFO: Connection successful! Account has 462 balances
INFO: Attempting to place MARKET order: BUY 0.001 BTCUSDT
INFO: Market order placed successfully. Order ID: 11862605
INFO: --- Order Response Details ---
INFO: Order ID: 11862605
INFO: Status: FILLED
INFO: Executed Quantity: 0.00100000
INFO: Status: SUCCESS

## Log Files

The logs/ folder contains two sample log files demonstrating successful order execution:

a. market_order.log - Shows a successful market buy order
b. limit_order.log - Shows a successful limit sell order

These logs include:

a. Order request details
b. API response information
c. Order ID, status, and execution details
d. Timestamps for audit trail

## Error Handling

The bot handles various error scenarios gracefully:

a. Invalid API keys - Clear error message, exit gracefully
b. Network issues - Log error, retry logic
c. Invalid input - Validation message, exit with code 1
d. Insufficient balance - API error captured and logged
e. Rate limiting - Binance API exception handled

## Dependencies

python-binance==1.0.19
python-dotenv==1.0.0
requests==2.31.0

## Security Notes

a. API keys are stored in .env file (excluded from Git via .gitignore)
b. No sensitive data is hardcoded in the source code
c. All API communication uses HTTPS
d. Log files contain no sensitive information

## Testing

a. Limit BUY orders (successful)
b. Limit SELL orders (successful)

## Contributing

This project was created as part of a Python Developer Intern assignment. Feel free to fork and enhance!

## License

MIT License - feel free to use this code for learning purposes.

## Acknowledgments

a. Binance for providing the Testnet environment
b. python-binance library developers
c. The open-source community

## 📧 Contact

- **Email**: pankaj.singh.me.eng@gmail.com
- **GitHub**: [Pankaj-Singh-10](https://github.com/Pankaj-Singh-10)
- **LinkedIn**: https://www.linkedin.com/in/pankaj-singh-4b108b2a2/
