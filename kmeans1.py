from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
Data={
    'x': [1.713,0.180,0.353,0.940,1.486,1.266,1.540,0.459,0.773],
    'y': [1.586,1.786,1.240,1.566,0.759,1.106,0.419,1.799,0.186]
}
df= DataFrame(Data,columns=['x','y'])
kmeans=KMeans(n_clusters=3).fit(df)
centroid=kmeans.cluster_centers_
print(centroid)
plt.scatter(df['x'],df['y'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroid[:,0],centroid[:,1],c='red',s=100)
plt.show()