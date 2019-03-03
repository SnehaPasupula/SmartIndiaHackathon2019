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
from operator import itemgetter

def preProcess(arr):
    a=[]
    b=arr[0]
    arr=arr[1:]
    final=[]
    for i in range(0,len(arr)):
       if(arr[i] is not None):
            if(arr[i][1] is not None and arr[i][0] is not None):
                a.append(arr[i])
            else:
                continue
    a=sorted(a, key=itemgetter(0))
    for i in range(0,len(a)):
        if(a[i][2]=='Kilograms'):
            a[i][1]=a[i][1]/1000
            a[i][2]='Tonnes'
        if(i>0):
            a[i][1]+=a[i-1][1]
    
    for i in range(0,len(a)-1):
        if((a[i][0]+1)!=a[i+1][0]):
            final.append(a[i])
            for j in range(1,(a[i+1][0]-a[i][0])):
                final.append([a[i][0]+j,a[i][1],a[i][2]])
        else:
            final.append(a[i])
    final.append(a[len(a)-1])
    return final





class toy:
    def predictions(self,datas):
        tooldata= pd.read_csv('Schools_and_toys.csv')
        tooldata1= pd.read_csv('Schools_and_toys.csv')
        self.x0=tooldata['plastic_waste'][:].values
        self.y1=tooldata['Co2_plastic_material'][:].values
        self.py1=tooldata1['Co2_plastic_material'][:].values
        self.y2=tooldata['methane_plastic'][:].values
        self.py2=tooldata1['methane_plastic'][:].values
        self.y3=tooldata['N2o_plastic'][:].values
        self.py3=tooldata1['N2o_plastic'][:].values
        self.py4=tooldata1['Recycle'][:].values
        self.py5=tooldata1['Discarded'][:].values
        self.py6=tooldata1['Incinerated'][:].values
        self.py7=tooldata1['Plastic_in_ocean'][:].values
        self.y4=tooldata['Recycle'][:].values
        self.y5=tooldata['Discarded'][:].values
        self.y6=tooldata['Incinerated'][:].values
        self.y7=tooldata['Plastic_in_ocean'][:].values
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
            k=data[0]-1990
            dump=data[1]+tooldata['plastic_waste'][k]
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
        tooldata= pd.read_csv('Schools_and_toys.csv')
        years=tooldata['Year']
        x1=[]
        for i in years:
            x1.append(int(i))
        y4=[]
        py4=[]
        for i in self.y4:
            y4.append(int(i))
        for i in self.py4:
            py4.append(int(i))
        x1=np.array(x1)
        y4=np.array(y4)
        py4=np.array(py4)
        trace1 = go.Scatter(
            x = x1,
            y = y4,
            mode = 'lines+markers',
            name = 'actual values',
            
        )
        trace2 = go.Scatter(
            x = x1,
            y = py4,
            mode = 'lines+markers',
            name = 'impact values'
        )
        layout= go.Layout(
            title= 'Recyled Toys and School materials',
            hovermode= 'closest',
            xaxis= dict(
                title= 'Year',
                ticklen= 1,
                zeroline= False,
                gridwidth= 1,
            ),
            yaxis=dict( 
                title= 'Recycle',
                ticklen= 5,
                gridwidth= 1,
            ),
            showlegend= True
        )
        data=[trace1,trace2]
        fig= go.Figure(data,layout=layout)
        plot(fig,filename='t&srecycle.html',auto_open=False)
        y5=[]
        py5=[]
        for i in self.y5:
            y5.append(int(i))
        for i in self.py5:
            py5.append(int(i))
        y5=np.array(y5)
        py5=np.array(py5)
        trace1 = go.Scatter(
            x = x1,
            y = y5,
            mode = 'lines+markers',
            name = 'actual values',
            
        )
        trace2 = go.Scatter(
            x = x1,
            y = py5,
            mode = 'lines+markers',
            name = 'impact values'
        )
        layout= go.Layout(
            title= 'Discarded Toys and School materials',
            hovermode= 'closest',
            xaxis= dict(
                title= 'Year',
                ticklen= 1,
                zeroline= False,
                gridwidth= 1,
            ),
            yaxis=dict( 
                title= 'Discarded',
                ticklen= 5,
                gridwidth= 1,
            ),
            showlegend= True
        )
        data=[trace1,trace2]
        fig= go.Figure(data,layout=layout)
        plot(fig,filename='t&sdiscarded.html',auto_open=False)
        y6=[]
        py6=[]
        for i in self.y6:
            y6.append(int(i))
        for i in self.py6:
            py6.append(int(i))
        y6=np.array(y6)
        py6=np.array(py6)
        trace1 = go.Scatter(
            x = x1,
            y = y6,
            mode = 'lines+markers',
            name = 'actual values',
            
        )
        trace2 = go.Scatter(
            x = x1,
            y = py6,
            mode = 'lines+markers',
            name = 'impact values'
        )
        layout= go.Layout(
            title= 'Incenerated Toy And School material',
            hovermode= 'closest',
            xaxis= dict(
                title= 'Year',
                ticklen= 1,
                zeroline= False,
                gridwidth= 1,
            ),
            yaxis=dict( 
                title= 'Incenerated',
                ticklen= 5,
                gridwidth= 1,
            ),
            showlegend= True
        )
        data=[trace1,trace2]
        fig= go.Figure(data,layout=layout)
        plot(fig,filename='t&sincenerated.html',auto_open=False)
        y7=[]
        py7=[]
        for i in self.y7:
            y7.append(int(i))
        for i in self.py7:
            py7.append(int(i))
        y7=np.array(y7)
        py7=np.array(py7)
        trace1 = go.Scatter(
            x = x1,
            y = y7,
            mode = 'lines+markers',
            name = 'actual values',
            
        )
        trace2 = go.Scatter(
            x = x1,
            y = py7,
            mode = 'lines+markers',
            name = 'impact values'
        )
        layout= go.Layout(
            title= 'Toy And School waste in ocean',
            hovermode= 'closest',
            xaxis= dict(
                title= 'Year',
                ticklen= 1,
                zeroline= False,
                gridwidth= 1,
            ),
            yaxis=dict( 
                title= 'Ocean waste',
                ticklen= 5,
                gridwidth= 1,
            ),
            showlegend= True
        )
        data=[trace1,trace2]
        fig= go.Figure(data,layout=layout)
        plot(fig,filename='t&socean.html',auto_open=False)
 
        



        
            
        
            
            
            
