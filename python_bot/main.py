from data_fetcher import DataFetcher
from feature_engineering import add_technical_indicators
from signal_generator import generate_signals
from trading_simulator import TradingSimulator
from utils import save_csv

def main():
    fetcher = DataFetcher()
    df = fetcher.fetch_historical()
    df = add_technical_indicators(df)
    df = generate_signals(df)

    simulator = TradingSimulator()
    final_value = simulator.run(df)

    print(f"Final portfolio value: ${final_value:.2f}")
    save_csv(df, "data/spy_signals.csv")
    print("Signals saved to data/spy_signals.csv")

if __name__ == "__main__":
    main()
