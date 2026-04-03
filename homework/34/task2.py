import time

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from skopt import BayesSearchCV


df = pd.read_csv("task2.csv")
df = pd.get_dummies(df).dropna()


X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, 20, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}
param_dist = {
    "n_estimators": [50, 100, 200, 300],
    "max_depth": [5, 10, 20, 30, None],
    "min_samples_split": [2, 5, 10, 15],
    "min_samples_leaf": [1, 2, 4, 6]
}


def run(model):
    start = time.time()
    model.fit(X_train, y_train)
    t = time.time() - start
    pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    return model.best_params_, rmse, t


grid = GridSearchCV(RandomForestRegressor(), param_grid, cv=3, n_jobs=-1)
rand = RandomizedSearchCV(RandomForestRegressor(), param_dist, n_iter=20, cv=3, n_jobs=-1)
bayes = BayesSearchCV(RandomForestRegressor(), param_dist, n_iter=20, cv=3, n_jobs=-1)


g_params, g_rmse, g_time = run(grid)
r_params, r_rmse, r_time = run(rand)
b_params, b_rmse, b_time = run(bayes)


print("GRID:", g_params, g_rmse, g_time)
print("RANDOM:", r_params, r_rmse, r_time)
print("BAYES:", b_params, b_rmse, b_time)
