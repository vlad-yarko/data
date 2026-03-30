import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

data = {
    'Income': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'Spending': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}
df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(df)
print(kmeans.labels_)
