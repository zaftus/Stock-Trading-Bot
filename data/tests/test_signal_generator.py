import pandas as pd
from python_bot.signal_generator import generate_signals

def test_signal_generator():
    df = pd.DataFrame({
        "SMA_10": [1, 2, 3, 2, 1],
        "SMA_50": [2, 2, 2, 2, 2]
    })
    df = generate_signals(df)
    assert all(df["Signal"].isin([-1,0,1]))
