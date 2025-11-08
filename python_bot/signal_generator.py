def generate_signals(df):
    df["Signal"] = 0
    df.loc[df["SMA_10"] > df["SMA_50"], "Signal"] = 1  # Buy
    df.loc[df["SMA_10"] < df["SMA_50"], "Signal"] = -1 # Sell
    return df
