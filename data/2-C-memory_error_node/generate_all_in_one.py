import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

df_payload = pd.read_csv('./data/last_payload.csv')
df_uptime_heat = pd.read_csv('./data/heatmap_uptime.csv')
df_nodes_heat = pd.read_csv('./data/heatmap_nodes.csv')

df_payload = df_payload.head(1000)
df_uptime_heat = df_uptime_heat.head(1000)
df_nodes_heat = df_nodes_heat.head(1000)

df_payload.sort_values(by=['Time'], inplace=True)

initial_time = 1592685206500
x = [(i - initial_time)/1000 for i in df_payload['Time']]

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                    row_heights=[400, 400], x_title="Time (s)",
                    subplot_titles=["Uptime (s)","Number of nodes allocated per device"])

# UPTIME
x_h = []
for i in df_uptime_heat['Time']:
    x_h.append(i)

cols = ["Device 1", "Device 2", "Device 3", "Device 4"]

c = df_uptime_heat.columns.values
c = np.delete(c, 0)
y = ["Device 1", "Device 2", "Device 3", "Device 4"]

z = []
for col in df_uptime_heat:
    if col == "Time":
        continue
    z.append(df_uptime_heat[col])

fig.add_trace(
    go.Heatmap(
        z=z,
        x0=2.5,
        dx=5,
        y=cols,
        xgap=1,
        ygap=1,
        text=z,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(140, 149, 255)']],
        yaxis="y1",
        showscale=False
    ),
    row=1, col=1
)

for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            fig.add_annotation(dict(
                text=str(z[n][m]),
                x=x_h[m]+2.5,
                y=y[n],
                xref='x',
                yref='y1',
                showarrow=False,
                font=dict(size=8)
            )
          )
# NR NODES
cols = ["Device 1", "Device 2", "Device 3", "Device 4"]

z = []
for col in df_nodes_heat:
    if col == "Time":
        continue
    z.append(df_nodes_heat[col])

fig.add_trace(
    go.Heatmap(
        z=z,
        x0=2.5,
        dx=5,
        y=cols,
        xgap=1,
        ygap=1,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(140, 149, 255)']],
        yaxis="y2",
        showscale=False
    ),
    row=2, col=1
)

for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            fig.add_annotation(dict(
                text=str(z[n][m]),
                x=x_h[m]+2.5,
                y=y[n],
                xref='x',
                yref='y2',
                showarrow=False,
                font=dict(size=8)
              )
            )

# Add figure title
fig.update_layout(
    font=dict(
        size=15
    ),
    xaxis=dict(
        dtick=5
    ),
    height=500,
    width=2500,
    margin=dict(
        t=45,
        b=20,
        l=0,
        r=0,
        pad=0
    ),
    legend=dict(
        orientation="h",
        x=0.5,
        y=-0.05,
        xanchor='center',
        yanchor='top'
    ),
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.update_xaxes(range=[-5, 470])
#fig.show()
fig.write_image("memory_failure.pdf")