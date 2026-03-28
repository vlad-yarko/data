import numpy as np
import pandas as pd
import plotly.graph_objects as go


np.random.seed(42)
n = 150


df = pd.DataFrame({
    "Feature1": np.random.randn(n),
    "Feature2": np.random.randn(n),
    "Feature3": np.random.randn(n),
    "Category": np.random.choice(["A", "B", "C"], n)
})


colors = {"A": "red", "B": "blue", "C": "green"}


fig = go.Figure()


for cat in ["A", "B", "C"]:
    mask = df["Category"] == cat
    fig.add_trace(go.Scatter3d(
        x=df.loc[mask, "Feature1"],
        y=df.loc[mask, "Feature2"],
        z=df.loc[mask, "Feature3"],
        mode="markers",
        name=f"Category {cat}",
        marker=dict(size=5, color=colors[cat], opacity=0.8)
    ))


fig.update_layout(
    title="3D Scatter",
    scene=dict(
        xaxis_title="Feature1",
        yaxis_title="Feature2",
        zaxis_title="Feature3"
    )
)


fig.show()
