import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv('./3-big_scenario/data/status_data.csv')
df = df.head(1050)

fig = go.Figure(data=[
    go.Bar(name='Active', x=df['Time'], y=df['Active']),
    go.Bar(name='Inactive', x=df['Time'], y=df['Inactive'])
])

fig.update_layout(
  barmode='stack',
  font=dict(
      size=15
  ),
  margin=dict(
      t=45,
      b=20,
      l=0,
      r=0,
      pad=0
  )
)

fig.update_xaxes(title_text="Time (s)")
fig.update_yaxes(title_text="Number of devices")

fig.write_image("status.pdf")
