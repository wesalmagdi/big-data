import sys
import pandas as pd
from sklearn.cluster import KMeans


file_path = sys.argv[1]

df = pd.read_csv(file_path)


df_numeric = df.select_dtypes(include=['int64', 'float64'])


if df_numeric.shape[1] < 2:
    print("Not enough numeric columns for clustering.")
    exit()


df_numeric = df_numeric.fillna(df_numeric.mean())


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(df_numeric)


df['cluster'] = clusters


counts = df['cluster'].value_counts().sort_index()


with open("clusters.txt", "w") as f:
    for cluster, count in counts.items():
        f.write(f"Cluster {cluster}: {count} samples\n")

print("Clustering completed. Results saved to clusters.txt")