import logging

logger = logging.getLogger("TradingSimulator")
logging.basicConfig(level=logging.INFO)

class TradingSimulator:
    def __init__(self, initial_cash=100000):
        self.cash = initial_cash
        self.shares = 0
        self.trades = []

    def run(self, df):
        for index, row in df.iterrows():
            if row["Signal"] == 1 and self.cash > 0:  # Buy
                self.shares = self.cash / row["Close"]
                self.cash = 0
                self.trades.append(f"Bought at {row['Close']}")
                logger.info(f"Bought at {row['Close']}")
            elif row["Signal"] == -1 and self.shares > 0:  # Sell
                self.cash = self.shares * row["Close"]
                self.shares = 0
                self.trades.append(f"Sold at {row['Close']}")
                logger.info(f"Sold at {row['Close']}")
        return self.cash + self.shares * df.iloc[-1]["Close"]
