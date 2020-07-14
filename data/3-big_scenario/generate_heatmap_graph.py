import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

df = pd.read_csv('./data/heatmap_nodes_20.csv')
df = df.head(10000)

x = []
for i in df['Time']:
    x.append(i)

cols = df.columns.values
cols = np.delete(cols, 0)

y = []
for c in cols:
    y.append(c[-2:])

z = []
z_text = []
for col in df:
    if col == "Time":
        continue
    z.append(df[col])

fig = go.Figure(data=go.Heatmap(
    z=z,
    x0=0,
    dx=20,
    y=y,
    showscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(140, 149, 255)']]))

annotations = []
for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            annotations.append(dict(
                text=str(z[n][m]),
                x=x[m],
                y=y[n],
                xref='x1',
                yref='y1',
                showarrow=False,
                font=dict(
                    size=14
                ))
            )

# Add figure title
fig.update_layout(
    height=900,
    width=500,
    font=dict(
        size=16
    ),
    yaxis=dict(
        dtick=1
    ),
    xaxis=dict(
        dtick=40
    ),
    margin=dict(
        t=45,
        b=20,
        l=0,
        r=0,
        pad=0
    ),
    legend=dict(
        font=dict(
            size=18,
            family="Source Code Pro"
        )
    ),
    annotations = annotations
)

# # Set x-axis title
fig.update_xaxes(title_text="Time (s)", range=[0,290])

# Set y-axes titles
fig.update_yaxes(title_text="Device")

# fig.show()
fig.write_image("nr_nodes_paper_1.pdf")
