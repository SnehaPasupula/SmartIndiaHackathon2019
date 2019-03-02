import operator

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv('clothdata.csv')
print(data)
x=data['commercial(co2 in tonnes)'][:21].values
print(x)
