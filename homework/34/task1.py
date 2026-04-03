import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("task1.csv", encoding="utf-8-sig")


for col in ["Gender", "SubscriptionType", "ContractLength"]:
    df[col] = LabelEncoder().fit_transform(df[col])


X = df.drop(columns="Churn")
y = df["Churn"]

X_scaled = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


grid = GridSearchCV(
    SVC(),
    {"C": [1, 10], "gamma": [0.1, 0.01]},
    cv=2,
    n_jobs=-1
)
grid.fit(X_train, y_train)


y_pred = grid.best_estimator_.predict(X_test)


print("Best:", grid.best_params_)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["NoChurn", "Churn"]))


cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["NoChurn", "Churn"], yticklabels=["NoChurn", "Churn"])
plt.title(f"Confusion Matrix | Best: C={grid.best_params_['C']}, gamma={grid.best_params_['gamma']}")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()
