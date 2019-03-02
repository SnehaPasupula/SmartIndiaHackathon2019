import operator
from operator import itemgetter
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
    def predictions(self,datas):
        clothdata= pd.read_csv('cloth$data.csv')
        clothdata1= pd.read_csv('cloth$data.csv')
        self.x0=clothdata['Cloth Waste'][:].values
        self.y1=clothdata['commercial(co2 in tonnes)'][:].values
        self.py1=clothdata1['commercial(co2 in tonnes)'][:].values
        self.y2=clothdata['commercial methane'][:].values
        self.py2=clothdata1['commercial methane'][:].values
        self.y3=clothdata['commercial(n2o)'][:].values
        self.py3=clothdata1['commercial(n2o)'][:].values
        self.py4=clothdata1['Recycled'][:].values
        self.py5=clothdata1['discarded'][:].values
        self.py6=clothdata1['incenerated'][:].values
        self.py7=clothdata1['waste in ocean'][:].values
        self.y4=clothdata['Recycled'][:].values
        self.y5=clothdata['discarded'][:].values
        self.y6=clothdata['incenerated'][:].values
        self.y7=clothdata['waste in ocean'][:].values
        self.x0 = self.x0[:, np.newaxis]
        self.y1 = self.y1[:, np.newaxis]
        self.y2 = self.y2[:, np.newaxis]
        self.y3 = self.y3[:, np.newaxis]
        self.y4 = self.y4[:, np.newaxis]
        self.y5 = self.y5[:, np.newaxis]
        self.y6 = self.y6[:, np.newaxis]
        self.y7 = self.y7[:, np.newaxis]
        self.py1= self.py1[:,np.newaxis]
        self.py2= self.py2[:,np.newaxis]
        self.py3= self.py3[:,np.newaxis]
        self.py4= self.py4[:,np.newaxis]
        self.py5= self.py5[:,np.newaxis]
        self.py6= self.py6[:,np.newaxis]
        self.py7= self.py7[:,np.newaxis]
        polynomial_features= PolynomialFeatures(degree=2)
        x0_poly = polynomial_features.fit_transform(self.x0)
        predx=[]
        model1 = LinearRegression()
        model2 = LinearRegression()
        model3 = LinearRegression()
        model4 = LinearRegression()
        model5 = LinearRegression()
        model6 = LinearRegression()
        model7 = LinearRegression()
        model1.fit(x0_poly, self.y1)
        model2.fit(x0_poly, self.y2)
        model3.fit(x0_poly, self.y3)
        model4.fit(x0_poly, self.y4)
        model5.fit(x0_poly, self.y5)
        model6.fit(x0_poly, self.y6)
        model7.fit(x0_poly, self.y7)
        diffsum=[0,0,0,0,0,0,0]
        y1p=model1.predict(x0_poly)
        y2p=model2.predict(x0_poly)
        y3p=model3.predict(x0_poly)
        y4p=model4.predict(x0_poly)
        y5p=model5.predict(x0_poly)
        y6p=model6.predict(x0_poly)
        y7p=model7.predict(x0_poly)
        error=[abs(y1p-self.y1),abs(y2p-self.y2),abs(y3p-self.y3),abs(y4p-self.y4),abs(y5p-self.y5),abs(y6p-self.y6),abs(y7p-self.y7)]
        j=datas[len(datas)-1][0]
        for data in datas:
            k=int(data[0])-1990
            dump=data[1]+clothdata['Cloth Waste'][k]
            predx=[[dump]]
            self.py1[k]=model1.predict(polynomial_features.fit_transform(predx))
            self.py2[k]=model2.predict(polynomial_features.fit_transform(predx))
            self.py3[k]=model3.predict(polynomial_features.fit_transform(predx))
            self.py4[k]=model4.predict(polynomial_features.fit_transform(predx))
            self.py5[k]=model5.predict(polynomial_features.fit_transform(predx))
            self.py6[k]=model6.predict(polynomial_features.fit_transform(predx))
            self.py7[k]=model7.predict(polynomial_features.fit_transform(predx))
            diffsum[0]=diffsum[0]+self.py1[k]-self.y1[k]+error[0][k]
            diffsum[1]=diffsum[1]+self.py2[k]-self.y2[k]+error[1][k]
            diffsum[2]=diffsum[2]+self.py3[k]-self.y3[k]+error[2][k]
            diffsum[3]=diffsum[3]+self.py4[k]-self.y4[k]+error[3][k]
            diffsum[4]=diffsum[4]+self.py5[k]-self.y5[k]+error[4][k]
            diffsum[5]=diffsum[5]+self.py6[k]-self.y6[k]+error[5][k]
            diffsum[6]=diffsum[6]+self.py7[k]-self.y7[k]+error[6][k]
        return diffsum
    def visualize(self):
        print("visualize called")
        clothdata= pd.read_csv('cloth$data.csv')
        years=clothdata['Year']
        x1=[]
        for i in years:
            x1.append(int(i))
        y1=[]
        py1=[]
        for i in self.y1:
            y1.append(int(i))
        for i in self.py1:
            py1.append(int(i))
        x1=np.array(x1)
        y1=np.array(y1)
        py1=np.array(py1)
        trace1 = go.Scatter(
            x = x1,
            y = y1,
            mode = 'lines+markers',
            name = 'actual values',
            
        )
        trace2 = go.Scatter(
            x = x1,
            y = py1,
            mode = 'lines+markers',
            name = 'impact values'
        )
        layout= go.Layout(
            title= 'Carbon Dioxide(Co2)',
            hovermode= 'closest',
            xaxis= dict(
                title= 'Year',
                ticklen= 1,
                zeroline= False,
                gridwidth= 1,
            ),
            yaxis=dict(
                title= 'Co2 emission',
                ticklen= 5,
                gridwidth= 1,
            ),
            showlegend= False
        )
        data=[trace1,trace2]
        fig= go.Figure(data, layout=layout)
        plot(fig,filename='co2.html',auto_open=False)



    





            

        
