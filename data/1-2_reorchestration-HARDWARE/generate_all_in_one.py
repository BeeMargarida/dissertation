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

initial_time = 1592521749000
x = [(i - initial_time)/1000 for i in df_payload['Time']]

fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.04,
                    row_heights=[400, 400, 400], x_title="Time (s)",
                    subplot_titles=["Payload Size (bytes)", "Uptime (s)","Number of nodes allocated per device"])

# Add traces
# PAYLOAD
fig.add_trace(
    go.Scatter(x=x, y=df_payload['192.168.1.179'], yaxis="y1", mode='lines+markers',
               name='Device 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['192.168.1.200'], yaxis="y1", mode='lines+markers',
               name='Device 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['192.168.1.206'], yaxis="y1", mode='lines+markers',
               name='Device 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['192.168.1.207'], yaxis="y1", mode='lines+markers',
               name='Device 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=1, col=1
)
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
        yaxis="y3",
        showscale=False
    ),
    row=3, col=1
)

for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            fig.add_annotation(dict(
                text=str(z[n][m]),
                x=x_h[m]+2.5,
                y=y[n],
                xref='x',
                yref='y3',
                showarrow=False,
                font=dict(size=8)
              )
            )

ranges_min=[10000]
ranges_max=[60000]
shapes=[]
for g in range(1,2):
    for t in x_h:
        shapes.append(
            dict(
                type="line",
                xref="x",
                yref="y%s" % g,
                x0=t,
                y0=ranges_min[g - 1],
                x1=t,
                y1=ranges_max[g - 1],
                line=dict(
                    color="dimgrey",
                    width=0.1
                )
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
    height=700,
    width=1500,
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
    shapes=shapes,
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.update_xaxes(range=[-5, 290])
#fig.show()
fig.write_image("reorchestration_phys.pdf")