import operator
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
np.random.seed(0)
class cloth:
    def pedictions(self,datas):
        clothdata= pd.read_csv('cloth$data.csv')
        clothdata1= pd.read_csv('cloth$data1.csv')
        x0=clothdata['Cloth Waste'][:].values
        y1=clothdata['commercial(co2 in tonnes)'][:].values
        py1=clothdata1['commercial(co2 in tonnes)'][:].values
        y2=clothdata['commercial methane'][:].values
        py2=clothdata1['commercial methane'][:].values
        y3=clothdata['commercial(n2o)'][:].values
        py3=clothdata1['commercial(n2o)'][:].values
        py4=clothdata1['Recycled'][:].values
        py5=clothdata1['discarded'][:].values
        py6=clothdata1['incenerated'][:].values
        py7=clothdata1['waste in ocean'][:].values
        y4=clothdata['Recycled'][:].values
        y5=clothdata['discarded'][:].values
        y6=clothdata['incenerated'][:].values
        y7=clothdata['waste in ocean'][:].values
        x0 = x0[:, np.newaxis]
        y1 = y1[:, np.newaxis]
        y2 = y2[:, np.newaxis]
        y3 = y3[:, np.newaxis]
        y4 = y4[:, np.newaxis]
        y5 = y5[:, np.newaxis]
        y6 = y6[:, np.newaxis]
        y7 = y7[:, np.newaxis]
        py1= py1[:,np.newaxis]
        py2= py2[:,np.newaxis]
        py3= py3[:,np.newaxis]
        py4= py4[:,np.newaxis]
        py5= py5[:,np.newaxis]
        py6= py6[:,np.newaxis]
        py7= py7[:,np.newaxis]
        polynomial_features= PolynomialFeatures(degree=2)
        x0_poly = polynomial_features.fit_transform(x0)
        predx=[]
        model1 = LinearRegression()
        model2 = LinearRegression()
        model3 = LinearRegression()
        model4 = LinearRegression()
        model5 = LinearRegression()
        model6 = LinearRegression()
        model7 = LinearRegression()
        model1.fit(x0_poly, y1)
        model2.fit(x0_poly, y2)
        model3.fit(x0_poly, y3)
        model4.fit(x0_poly, y4)
        model5.fit(x0_poly, y5)
        model6.fit(x0_poly, y6)
        model7.fit(x0_poly, y7)
        diffsum=[0,0,0,0,0,0,0]
        y1p=model1.predict(x0_poly)
        y2p=model2.predict(x0_poly)
        y3p=model3.predict(x0_poly)
        y4p=model4.predict(x0_poly)
        y5p=model5.predict(x0_poly)
        y6p=model6.predict(x0_poly)
        y7p=model7.predict(x0_poly)
        error=[abs(y1p-y1),abs(y2p-y2),abs(y3p-y3),abs(y4p-y4),abs(y5p-y5),abs(y6p-y6),abs(y7p-y7)]
        print(error)
        for data in datas:
            dump=data[1]+clothdata['Cloth Waste'][data[0]-1990]
            predx.append([dump])
            k=data[0]-1990
            py1[k]=model1.predict(polynomial_features.fit_transform(predx))
            py2[k]=model2.predict(polynomial_features.fit_transform(predx))
            py3[k]=model3.predict(polynomial_features.fit_transform(predx))
            py4[k]=model4.predict(polynomial_features.fit_transform(predx))
            py5[k]=model5.predict(polynomial_features.fit_transform(predx))
            py6[k]=model6.predict(polynomial_features.fit_transform(predx))
            py7[k]=model7.predict(polynomial_features.fit_transform(predx))
            diffsum[0]=diffsum[0]+py1[k]-y1[k]+error[0][k]
            diffsum[1]=diffsum[1]+py2[k]-y2[k]+error[1][k]
            diffsum[2]=diffsum[2]+py3[k]-y3[k]+error[2][k]
            diffsum[3]=diffsum[3]+py4[k]-y4[k]+error[3][k]
            diffsum[4]=diffsum[4]+py5[k]-y5[k]+error[4][k]
            diffsum[5]=diffsum[5]+py6[k]-y6[k]+error[5][k]
            diffsum[6]=diffsum[6]+py7[k]-y7[k]+error[6][k]
        return diffsum


        


        
            
        
            
            
            
