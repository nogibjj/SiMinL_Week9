from mylib.lib import load, summary
import yfinance as yf
import warnings

warnings.filterwarnings("ignore")

natgas = yf.Ticker("NG=F")
df = natgas.history(interval="1d", start="2024-01-02")


def test_load(df):
    df = load(df)
    assert df is not None


def test_summary(df):
    summary_test = summary(df)
    assert summary_test.shape == (8, 7)


if __name__ == "__main__":
    test_load(df)
    test_summary(df)
