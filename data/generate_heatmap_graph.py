import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

df = pd.read_csv('./3-big_scenario/data/heatmap_nodes.csv')
df = df.head(10000)


x = []
for i in df['Time']:
    x.append(i)

cols = df.columns.values
cols = np.delete(cols, 0)

y = []
for c in cols:
    y.append(c)

z = []
z_text = []
for col in df:
    if col == "Time":
        continue
    z.append(df[col])

# for i in z:
#     z_t = []
#     for val in i:
#         if val > 0:
#             z_t.append(val)
#         else:
#             z_t.append(" ")
#     z_text.append(z_t)

annotations = go.Annotations()
for n, row in enumerate(z):
    for m, val in enumerate(row):
        if val > 0:
          annotations.append(go.Annotation(text=str(z[n][m]), x=x[m], y=y[n],
                                         xref='x1', yref='y1', showarrow=False, font=dict(
        size=8
    )))

fig = go.Figure(data=go.Heatmap(
  z=z,
  x0=0,
  dx=5,
  y=cols,
  colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(99,110,250)']]))

# fig = ff.create_annotated_heatmap(
#     z,
#     x=x,
#     y=y,
#     annotation_text=z_text,
#     xgap=1,
#     ygap=1,
#     colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(99,110,250)']]
# )


# Add figure title
fig.update_layout(
    title_text="Number of nodes allocated grouped by device",
    height=1000,
    width=2000,
    margin=dict(
        t=45,
        b=20,
        l=0,
        r=0,
        pad=0
    ),
    legend=dict(
        font=dict(
            size=15,
            family="Source Code Pro"
        )
    ),
    annotations=annotations,
    xaxis_nticks=60
)

# # Set x-axis title
fig.update_xaxes(title_text="Time (s)")

# Set y-axes titles
# fig.update_yaxes(title_text="Number of nodes allocated grouped by device", secondary_y=False)

#fig.show()
fig.write_image("nr_nodes.pdf")