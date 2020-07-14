import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

df = pd.read_csv('./data/heatmap_nodes_10.csv')
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

# 1. create two subplots
f, (ax, ax2) = plt.subplots(1, 2, sharey=True, facecolor='w')

# 2. plot the same data on both axes
#ax.bar(x, y)
#ax2.bar(x, y)

# im = ax.imshow(z, cmap=mpl.cm.Blues)
# im = ax2.imshow(z, cmap=mpl.cm.Blues)

# sns.heatmap(z, xticklabels=10, ax=ax, cmap=mpl.cm.Blues, cbar=False, annot=True)
# sns.heatmap(z, xticklabels=10, ax=ax2, cmap=mpl.cm.Blues, cbar=False, annot=True)

# 3. limit each x axis to the chosen range
a = 0
b = 2
c = 2
d = 10
ax.set_xlim(a, b)
ax2.set_xlim(c, d)
# ax.set_xlim(0,3)
# ax2.set_xlim(5.5,12.5)

# 4. hide the spines between ax and ax2
ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax.yaxis.tick_left()
ax.tick_params(labelright='off')
ax2.yaxis.tick_right()

# 5. This looks pretty good, and was fairly painless, but you can get that
# cut-out diagonal lines look with just a bit more work. The important
# thing to know here is that in axes coordinates, which are always
# between 0-1, spine endpoints are at these locations (0,0), (0,1),
# (1,0), and (1,1).  Thus, we just need to put the diagonals in the
# appropriate corners of each of our axes, and so long as we use the
# right transform and disable clipping.

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d, 1+d), (-d, +d), **kwargs)
ax.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
ax2.plot((-d, +d), (-d, +d), **kwargs)

# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'

# 6. Make some labels.
# rects = ax.patches
# labels = ["%d" % i for i in y]
# for i, rect, label in zip(x, rects, labels):
#     height = rect.get_height()
#     print(i)
#     if i < b:
#         ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
#                 ha='center', va='bottom')
#     elif i > c:
#         ax2.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
#                  ha='center', va='bottom')


# for n, row in enumerate(z):
#     for m, val in enumerate(row):
#         if val > 0:
#             text = ax.text(m, n, str(z[n][m]),
#                         ha="center", va="center", color="w")

plt.show()
