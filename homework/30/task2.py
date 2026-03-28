#NOTE: plotly does not have built in 3D histogram


import numpy as np
import plotly.graph_objects as go


np.random.seed(42)
n = 500
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)


hist, xedges, yedges = np.histogram2d(x, y, bins=20)


x_centers = (xedges[:-1] + xedges[1:]) / 2
y_centers = (yedges[:-1] + yedges[1:]) / 2


fig = go.Figure(data=[go.Surface(
    x=x_centers,
    y=y_centers,
    z=hist.T,
    colorscale='Blues',
    colorbar=dict(title='Count')
)])


fig.update_layout(
    title='3D Histogram',
    scene=dict(
        xaxis_title='X Value',
        yaxis_title='Y Value',
        zaxis_title='Count'
    )
)

fig.show()
