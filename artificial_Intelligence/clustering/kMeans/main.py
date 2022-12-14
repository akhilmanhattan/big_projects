"""
The purpose of this program is to create a program out of data that will cluster it into groups. That is KMeansClustering.

K Means clustering uses centroids that will be used to cluster the data. This is an unsupervised learning algorithm meaning that essentially, all that is happening
is that we are finding patterns between the two parameters: age and salary.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import Normalizer # Normalization is a scaling technique that is in reference with the mean of a data set.
from sklearn.cluster import KMeans
import matplotlib.pyplot as ppt

data = pd.read_csv(r"CollegeAndAgeInJob.csv")
x = data.iloc[:,:].values
xtn,xtt = tts(x,test_size=0.25,random_state=4)

#Normalizing the data because there are clusters
norm = Normalizer()
nxtn,nxtt = norm.fit_transform(xtn),norm.fit_transform(xtt)

model = KMeans(n_clusters=5,random_state=4)# Number of clusters determined using elbow method
model.fit(nxtn)

tncluster_pred = model.predict(nxtn)
ttcluster_pred = model.predict(nxtt)

# Training set time
for index in range(len(tncluster_pred)):
    pred = tncluster_pred[index]
    if pred == 0:
        ppt.plot(xtn[index,0],xtn[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#9467bd')
    elif pred == 1:
        ppt.plot(xtn[index,0],xtn[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#d62728')
    elif pred == 2:
        ppt.plot(xtn[index,0],xtn[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#2ca02c')
    elif pred == 3:
        ppt.plot(xtn[index,0],xtn[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#ff7f0e')
    elif pred == 4:
        ppt.plot(xtn[index,0],xtn[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#1f77b4')
        
ppt.xlabel('Age')
ppt.ylabel('Years in College')
ppt.title('Age vs Years In College Clusters')
ppt.savefig('KMeansTrainingSet.png')
ppt.clf()

# Test set time
for index in range(len(ttcluster_pred)):
    pred = ttcluster_pred[index]
    if pred == 0:
        ppt.plot(xtt[index,0],xtt[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#9467bd')
    elif pred == 1:
        ppt.plot(xtt[index,0],xtt[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#d62728')
    elif pred == 2:
        ppt.plot(xtt[index,0],xtt[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#2ca02c')
    elif pred == 3:
        ppt.plot(xtt[index,0],xtt[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#ff7f0e')
    elif pred == 4:
        ppt.plot(xtt[index,0],xtt[index,1],marker="o", markersize=10, markeredgecolor="red",markerfacecolor='#1f77b4')
        
ppt.xlabel('Age')
ppt.ylabel('Years in College')
ppt.title('Age vs Years In College Clusters')
ppt.savefig('KMeansTestSet.png')
