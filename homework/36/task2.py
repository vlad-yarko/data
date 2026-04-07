from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import plotly.graph_objects as go


y_true = [85, 90, 78, 92, 88, 76, 95, 89, 87, 91, 45]
y_pred = [83, 88, 80, 90, 86, 78, 93, 87, 85, 89, 70]


mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)


go.Figure(
    go.Bar(
        x=["MSE", "RMSE", "MAE", "R²"], y=[mse, rmse, mae, r2], marker_color="#3498db"
    )
).show()
