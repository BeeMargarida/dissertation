import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv('data/alloc_ram.csv')
print(df.head(902))
df = df.head(902)

fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces

fig.add_trace(
    go.Scatter(x = df['Time'], y = df['0c1fc2bd43ce'], mode='lines+markers',
                  name='0c1fc2bd43ce', connectgaps=True),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x = df['Time'], y = df['1edc5b28299f'], mode='lines+markers',
                  name='1edc5b28299f', connectgaps=True),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x = df['Time'], y = df['363f08b924c2'], mode='lines+markers',
                  name='363f08b924c2', connectgaps=True),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x = df['Time'], y = df['5118fb10a251'], mode='lines+markers',
                  name='5118fb10a251', connectgaps=True),
    secondary_y=False,
)

# Add figure title
fig.update_layout(
    title_text="Alloc RAM"
)

# Set x-axis title
fig.update_xaxes(title_text="Time")

# Set y-axes titles
fig.update_yaxes(title_text="Alloc RAM", secondary_y=False)

fig.show()