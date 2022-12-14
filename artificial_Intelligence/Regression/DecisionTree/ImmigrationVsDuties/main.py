"""
My sources for this Decision Tree Regressio's Data:

https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-
https://fraser.stlouisfed.org/files/docs/publications/histstatus/pages/1975-1979/58477_1975-1979.pdf
https://www.migrationpolicy.org/programs/data-hub/charts/immigrant-population-over-time
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeRegressor as dtr
import matplotlib.pyplot as ppt

data = pd.read_csv(r"iif.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# Test Training Split
xtn,xtt,ytn,ytt = tts(x,y,test_size=0.25,random_state=4)

# Making the model
model = DecisionTreeRegressor(max_depth = 57)
model.fit(xtn,ytn) # R-Squared value is 0.969563701289449

# I will make a graph for import duties (predicted) by this model from 1970 as data doesn't exist in the source
