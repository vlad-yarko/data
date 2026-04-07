import plotly.graph_objects as go


metrics = ["MSE", "RMSE", "MAE", "R²"]
model_a = [50, 7.07, 5, 0.85]
model_b = [80, 8.94, 6, 0.78]


fig = go.Figure(
    data=[
        go.Bar(name="Model A", x=metrics, y=model_a, marker_color="#2ecc71"),
        go.Bar(name="Model B", x=metrics, y=model_b, marker_color="#e74c3c"),
    ]
)
fig.update_layout(title="Model Comparison", barmode="group", yaxis_title="Value")
fig.show()
