import plotly.io as pio
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

df_alloc = pd.read_csv('./data/alloc_ram.csv')
df_free = pd.read_csv('./data/free_ram.csv')
df_flash = pd.read_csv('./data/flash_size.csv')
df_payload = pd.read_csv('./data/last_payload.csv')
df_uptime_heat = pd.read_csv('./data/heatmap_uptime_10.csv')
df_nodes_heat = pd.read_csv('./data/heatmap_nodes_10.csv')

df_alloc = df_alloc.head(902)
df_free = df_free.head(1000)
df_flash = df_flash.head(1000)
df_payload = df_payload.head(1000)
df_uptime_heat = df_uptime_heat.head(1000)
df_nodes_heat = df_nodes_heat.head(1000)

initial_time = 1592505318000
x = [(i - initial_time)/1000 for i in df_alloc['Time']]

for col in df_alloc:
    if col != "Time": 
        df_alloc[col] = df_alloc[col].div(1000)
        df_payload[col] = df_payload[col].div(1000)
        df_free[col] = df_free[col].div(1000)
    

fig = make_subplots(rows=6, cols=1, shared_xaxes=True, vertical_spacing=0.04,
                    row_heights=[400, 400, 400, 400, 400, 400], x_title="Time (s)",
                    subplot_titles=["RAM allocated (Kbytes)", "Free RAM (Mbytes)", "Free Flash Space (bytes)",
                                    "Payload Size (Kbytes)", "Uptime (s)", "Number of nodes allocated per device"],
                    specs=[[{"type": "xy"}], [{"type": "xy"}], [{"type": "xy"}], [{"type": "xy"}], [{"type": "heatmap"}], [{"type": "heatmap"}]])

# Add traces
# ALLOC RAM
fig.add_trace(
    go.Scatter(x=x, y=df_alloc['192.168.1.165'], yaxis="y1", mode='lines+markers',
               name='Dev. 1', line=dict(color='#636efa', width=2), connectgaps=True), row=1, col=1,
)

fig.add_trace(
    go.Scatter(x=x, y=df_alloc['192.168.1.179'], yaxis="y1", mode='lines+markers',
               name='Dev. 2', line=dict(color='#ef553b', width=2), connectgaps=True), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_alloc['192.168.1.200'], yaxis="y1", mode='lines+markers',
               name='Dev. 3', line=dict(color='#00cc96', width=2), connectgaps=True), row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_alloc['192.168.1.206'], yaxis="y1", mode='lines+markers',
               name='Dev. 4', line=dict(color='#ab63fa', width=2), connectgaps=True), row=1, col=1
)
# FREE RAM
fig.add_trace(
    go.Scatter(x=x, y=df_free['192.168.1.165'], yaxis="y2", mode='lines+markers',
               name='Dev. 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_free['192.168.1.179'], yaxis="y2", mode='lines+markers',
               name='Dev. 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_free['192.168.1.200'], yaxis="y2", mode='lines+markers',
               name='Dev. 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_free['192.168.1.206'], yaxis="y2", mode='lines+markers',
               name='Dev. 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=2, col=1
)
# FLASH
fig.add_trace(
    go.Scatter(x=x, y=df_flash['192.168.1.165'], yaxis="y3", mode='lines+markers',
               name='Dev. 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_flash['192.168.1.179'], yaxis="y3", mode='lines+markers',
               name='Dev. 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_flash['192.168.1.200'], yaxis="y3", mode='lines+markers',
               name='Dev. 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_flash['192.168.1.206'], yaxis="y3", mode='lines+markers',
               name='Dev. 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=3, col=1
)
# PAYLOAD
x_payload = [(i - initial_time)/1000 for i in df_payload['Time']]
fig.add_trace(
    go.Scatter(x=x_payload, y=df_payload['192.168.1.165'], yaxis="y4", mode='lines+markers',
               name='Dev. 1', line=dict(color='#636efa', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)

fig.add_trace(
    go.Scatter(x=x_payload, y=df_payload['192.168.1.179'], yaxis="y4", mode='lines+markers',
               name='Dev. 2', line=dict(color='#ef553b', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)

fig.add_trace(
    go.Scatter(x=x_payload, y=df_payload['192.168.1.200'], yaxis="y4", mode='lines+markers',
               name='Dev. 3', line=dict(color='#00cc96', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)

fig.add_trace(
    go.Scatter(x=x_payload, y=df_payload['192.168.1.206'], yaxis="y4", mode='lines+markers',
               name='Dev. 4', line=dict(color='#ab63fa', width=2),
               connectgaps=True, showlegend=False), row=4, col=1
)
# UPTIME

x_h = []
for i in df_uptime_heat['Time']:
    x_h.append(i)

cols = ["Dev. 1", "Dev. 2", "Dev. 3", "Dev. 4"]

y = ["Dev. 1", "Dev. 2", "Dev. 3", "Dev. 4"]

z = []
for col in df_uptime_heat:
    if col == "Time":
        continue
    z.append(df_uptime_heat[col])

fig.add_trace(
    go.Heatmap(
        z=z,
        x0=0,
        dx=10,
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
                text=str(int(z[n][m])),
                x=x_h[m],
                y=y[n],
                xref='x',
                yref='y5',
                showarrow=False,
                font=dict(size=16)
            )
          )
# NR NODES
z = []
for col in df_nodes_heat:
    if col == "Time":
        continue
    z.append(df_nodes_heat[col])

fig.add_trace(
    go.Heatmap(
        z=z,
        x0=0,
        dx=10,
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
                text=str(int(z[n][m])),
                x=x_h[m],
                y=y[n],
                xref='x',
                yref='y6',
                showarrow=False,
                font=dict(size=16)
            )
            )

ranges_min=[0,0,2015,13.13]
ranges_max=[200,100,2040,18]
shapes=[]
for g in range(1,5):
    for t in range(0, 360, 50):
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
        size=18
    ),
    height=1000,
    width=1200,
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

fig.update_xaxes(range=[-5, 350])
#fig.show()
fig.write_image("sanity_check_hardware.pdf")
#files.download('sanity_check_hardware.pdf')