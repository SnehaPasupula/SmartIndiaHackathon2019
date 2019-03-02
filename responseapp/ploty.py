import operator
import flask
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import dash
import dash_core_components as dcc
import dash_html_components as html
#server=flassk.Flask(__name__)
#app=dash.Dash(__name__,server=server)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv('cloth$data.csv') 

np.random.seed(0)
#x = 2 - 3 * np.random.normal(0, 1, 20)
#y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
print(data)
x=data['Total plastic waste '][:].values
y = data['Residential & commercial (tonnes)'][:].values
x1=data['Total plastic waste '][:].values
x2=data['Total plastic waste '][2014-1990]
print(x2)

# transforming the data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]
x1 = x1[:, np.newaxis]


polynomial_features= PolynomialFeatures(degree=1)
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

#rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
#r2 = r2_score(y,y_poly_pred)
#print(rmse)
#print(r2)


#model.predict(polynomial_features.fit_transform(0.5))
k=model.predict(polynomial_features.fit_transform(x1))
p=[]
for i in k:
        for j in i:
            value=str(j)
            value2=value.replace(',', '.')
            print(value2)
            p.append(value2)
        
print(model.predict(polynomial_features.fit_transform(x)))
plt.scatter(x, y, s=20)
# sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
k=plt.plot(x, y_poly_pred, color='m')
plt.show()


