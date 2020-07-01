import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

df_payload = pd.read_csv('./data/last_payload.csv')
df_uptime_heat = pd.read_csv('./data/heatmap_uptime_10.csv')
df_nodes_heat = pd.read_csv('./data/heatmap_nodes_10.csv')

df_payload = df_payload.head(1000)
df_uptime_heat = df_uptime_heat.head(1000)
df_nodes_heat = df_nodes_heat.head(1000)

df_payload.sort_values(by=['Time'], inplace=True)

initial_time = 1592665552000
x = [(i - initial_time)/1000 for i in df_payload['Time']]

for col in df_payload:
    if col != "Time":
        df_payload[col] = df_payload[col].div(1000)

fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.04,
                    row_heights=[400, 400, 400], x_title="Time (s)",
                    subplot_titles=["Payload Size (Kbytes)", "Uptime (s)", "Number of nodes allocated per device"])

# PAYLOAD
fig.add_trace(
    go.Scatter(x=x, y=df_payload['481714f496e4'], yaxis="y1", mode='lines+markers',
               name='Dev. 1', line=dict(color='#636efa', width=2), connectgaps=True),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['6f2c053265f6'], yaxis="y1", mode='lines+markers',
               name='Dev. 2', line=dict(color='#ef553b', width=2), connectgaps=True),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['78034b84ad0f'], yaxis="y1", mode='lines+markers',
               name='Dev. 3', line=dict(color='#00cc96', width=2), connectgaps=True),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=df_payload['8d2d383ac982'], yaxis="y1", mode='lines+markers',
               name='Dev. 4', line=dict(color='#ab63fa', width=2), connectgaps=True),
    row=1, col=1
)

# UPTIME
x_h = []
for i in df_uptime_heat['Time']:
    x_h.append(i)

cols = ["Dev. 1", "Dev. 2", "Dev. 3", "Dev. 4"]

c = df_uptime_heat.columns.values
c = np.delete(c, 0)
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
                x=x_h[m],
                y=cols[n],
                xref='x',
                yref='y2',
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
                x=x_h[m],
                y=cols[n],
                xref='x',
                yref='y3',
                showarrow=False,
                font=dict(size=16)
            )
            )

shapes = []
for t in range(0, 210, 50):
    shapes.append(
        dict(
            type="line",
            xref="x",
            yref="y1",
            x0=t,
            y0=0,
            x1=t,
            y1=27,
            line=dict(
                color="dimgrey",
                width=0.1
            )
        )
    )

shapes.append(
    # Line Vertical
    dict(
        type="line",
        xref="x",
        yref="y1",
        x0=79.2,
        y0=0,
        x1=79.2,
        y1=27,
        line=dict(
            color="Black",
            width=1
        )
    ))

shapes.append(
    # Line Vertical
    dict(
        type="line",
        xref="x",
        yref="y1",
        x0=112.2,
        y0=0,
        x1=112.2,
        y1=27,
        line=dict(
            color="Black",
            width=1
        )
    ))

fig.add_annotation(
    dict(
        x=79,
        y=26,
        xref="x",
        yref="y1",
        text="Dev. 2 failure",
        showarrow=False,
        xanchor="right",
        align="right"
    )
)
fig.add_annotation(
    dict(
        x=113,
        y=26,
        xref="x",
        yref="y1",
        text="Dev. 2 recovery",
        showarrow=False,
        xanchor="left",
        align="right"
    )
)

# Add figure title
fig.update_layout(
    font=dict(
        size=18
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

fig.update_xaxes(range=[-5, 210])
# fig.show()
fig.write_image("memory_write.pdf")
