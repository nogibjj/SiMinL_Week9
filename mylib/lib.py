import matplotlib.pyplot as plt
import plotly.graph_objects as go  # Import the data visualization tool plotly
from plotly.subplots import make_subplots  # Import make_subplots for subplots

# natgas = yf.Ticker("NG=F")
# df = natgas.history(interval="1d", start="2024-01-02")


# loading dataset
def load(df):
    return df


# summarize the data
def summary(df):
    data_summary = df.describe()
    print(data_summary)
    print(data_summary.shape)
    return data_summary


# data visualisation
def chart(df):
    plt.figure(figsize=(10, 4))
    plt.plot(df["Close"], linewidth=1.5, color="b")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()


def candlestick(df):
    cstick = go.Candlestick(
        x=df.index,  # Dates as x data
        open=df["Open"],  # Open prices
        close=df["Close"],  # Close prices
        high=df["High"],  # High prices
        low=df["Low"],  # Low prices
        name="NAT_GAS",
    )  # Label of the graph

    figure = go.Figure()  # Create a Figure
    figure.add_trace(cstick)  # Attach the graph to the figure
    figure.show()

    figure = make_subplots(specs=[[{"secondary_y": True}]])

    cstick = go.Candlestick(
        x=df.index,  # Dates as x data
        open=df["Open"],  # Open prices
        close=df["Close"],  # Close prices
        high=df["High"],  # High prices
        low=df["Low"],  # Low prices
        name="NAT_GAS",
    )  # Label of the graph

    maline1 = go.Scatter(
        x=df.index,
        y=df["Close"].rolling(5).mean(),
        line={"color": "blue", "width": 1},
        name="5-day moving average",
    )
    maline2 = go.Scatter(
        x=df.index,
        y=df["Close"].rolling(10).mean(),
        line={"color": "orange", "width": 1},
        name="10-day moving average",
    )
    vbar = go.Bar(x=df.index, y=df["Volume"], name="Volume")

    figure.add_trace(cstick)  # Attach the candelstick to the figure
    figure.add_trace(maline1)  # Attach the MA curve to the figure
    figure.add_trace(maline2)  # Attach the MA curve to the figure
    figure.add_trace(vbar, secondary_y=True)  # Attach the volume bar to the figure

    figure.update_yaxes(
        range=[0, 11], title="Price", secondary_y=False
    )  # Properties of the y-axis on the left
    figure.update_yaxes(
        range=[0, 8e8],
        tickvals=list(range(0, 200000000, 50000000)),
        showgrid=False,
        title="Volume",
        secondary_y=True,
    )  # Properties of the y-axis on the right
    figure.show()
