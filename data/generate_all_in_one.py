import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

df_alloc = pd.read_csv('./1-sanity_check/data/alloc_ram.csv')
df_free = pd.read_csv('./1-sanity_check/data/free_ram.csv')
df_flash = pd.read_csv('./1-sanity_check/data/flash_size.csv')
df_payload = pd.read_csv('./1-sanity_check/data/last_payload.csv')
df_uptime_heat = pd.read_csv('./1-sanity_check/data/heatmap_uptime.csv')
df_nodes_heat = pd.read_csv('./1-sanity_check/data/heatmap_nodes.csv')
df_communications_heat = pd.read_csv(
    './1-sanity_check/data/heatmap_communications.csv')

df_alloc = df_alloc.head(902)
df_free = df_free.head(1000)
df_flash = df_flash.head(1000)
df_payload = df_payload.head(1000)
df_uptime_heat = df_uptime_heat.head(1000)
df_nodes_heat = df_nodes_heat.head(1000)
df_communications_heat = df_communications_heat.head(1000)

initial_time = 1592334346200
x = [(i - initial_time)/1000 for i in df_alloc['Time']]

fig = make_subplots(rows=7, cols=1, shared_xaxes=True, vertical_spacing=0.04,
                    row_heights=[400, 400, 400, 400, 400, 400, 400], x_title="Time (s)",
                    subplot_titles=["RAM allocated (bytes)", "Free RAM (bytes)", "Flash Size (bytes)", "Payload Size (bytes)", "Uptime (s)",
                                    "Number of nodes allocated per device", "Number of messages exchanged per device"],
                    specs=[[{"type": "xy"}], [{"type": "xy"}], [{"type": "xy"}], [{"type": "xy"}], [{"type": "xy"}], [{"type": "heatmap"}], [{"type": "xy"}]])

# Add traces
# ALLOC RAM
fig.add_trace(
    go.Scatter(x=x, y=df_alloc['188e2a5d583c'], yaxis="y1", mode='lines+markers',
               name='Device 1', line=dict(color='#636efa', width=2), connectgaps=True), row=1, col=1,
)

fig.add_trace(
    go.Scatter(x=x, y=df_alloc['26f29effeddc'], yaxis="y1", mode='lines+markers',
               name='Device 2', line=dict(color='#ef553b', width=2), connectgaps=True), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_alloc['4b86a2021b77'], yaxis="y1", mode='lines+markers',
               name='Device 3', line=dict(color='#00cc96', width=2), connectgaps=True), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_alloc['8f96fa542f8b'], yaxis="y1", mode='lines+markers',
               name='Device 4', line=dict(color='#ab63fa', width=2), connectgaps=True), row=1, col=1
)
# FREE RAM
fig.add_trace(
    go.Scatter(x=x, y=df_free['188e2a5d583c'], yaxis="y2", mode='lines+markers',
               name='Device 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_free['26f29effeddc'], yaxis="y2", mode='lines+markers',
               name='Device 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_free['4b86a2021b77'], yaxis="y2", mode='lines+markers',
               name='Device 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_free['8f96fa542f8b'], yaxis="y2", mode='lines+markers',
               name='Device 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)
# FLASH
fig.add_trace(
    go.Scatter(x=x, y=df_flash['188e2a5d583c'], yaxis="y3", mode='lines+markers',
               name='Device 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_flash['26f29effeddc'], yaxis="y3", mode='lines+markers',
               name='Device 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_flash['4b86a2021b77'], yaxis="y3", mode='lines+markers',
               name='Device 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_flash['8f96fa542f8b'], yaxis="y3", mode='lines+markers',
               name='Device 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)
# PAYLOAD
fig.add_trace(
    go.Scatter(x=x, y=df_payload['188e2a5d583c'], yaxis="y4", mode='lines+markers',
               name='Device 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['26f29effeddc'], yaxis="y4", mode='lines+markers',
               name='Device 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['4b86a2021b77'], yaxis="y4", mode='lines+markers',
               name='Device 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['8f96fa542f8b'], yaxis="y4", mode='lines+markers',
               name='Device 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)
# UPTIME

x_h = []
for i in df_uptime_heat['Time']:
    x_h.append(i)

cols = ["Device 1", "Device 2", "Device 3", "Device 4"]

c = df_communications_heat.columns.values
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
        yaxis="y5",
        showscale=False
    ),
    row=5, col=1
)

for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            fig.add_annotation(dict(
                text=str(z[n][m]),
                x=x_h[m]+2.5,
                y=y[n],
                xref='x',
                yref='y5',
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
        yaxis="y6",
        showscale=False
    ),
    row=6, col=1
)

for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            fig.add_annotation(dict(
                text=str(z[n][m]),
                x=x_h[m]+2.5,
                y=y[n],
                xref='x',
                yref='y6',
                showarrow=False,
                font=dict(size=8)
            )
            )
# COMMUNICATIONS
cols = ["Device 1", "Device 2", "Device 3", "Device 4"]

z = []
for col in df_communications_heat:
    if col == "Time":
        continue
    z.append(df_communications_heat[col])

z_text = []
for i in z:
    z_t = []
    for val in i:
        if val > 0:
            z_t.append(val)
        else:
            z_t.append(" ")
    z_text.append(z_t)

fig.add_trace(
    go.Heatmap(
        z=z,
        x0=2.5,
        dx=5,
        y=cols,
        xgap=1,
        ygap=1,
        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(140, 149, 255)']],
        yaxis="y7",
        showscale=False
    ),
    row=7, col=1
)

for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
            fig.add_annotation(dict(
                text=str(z[n][m]),
                x=x_h[m]+2.5,
                y=y[n],
                xref='x',
                yref='y7',
                showarrow=False,
                font=dict(size=8)
            )
            )

ranges_min=[50000,1850000,39450000,13500]
ranges_max=[200000,2100000,39600000,16000]
shapes=[]
for g in range(1,5):
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
    height=1000,
    width=1000,
    margin=dict(
        t=45,
        b=20,
        l=0,
        r=0
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

fig.update_xaxes(range=[-5, 145])

# fig.show()
fig.write_image("sanity_check.pdf")
# files.download('sanity_check.pdf')
