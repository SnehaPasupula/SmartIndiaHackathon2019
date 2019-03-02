import pandas as pd
import numpy as np
from io import StringIO
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn.linear_model import LinearRegression
from plotly import tools
frame=pd.read_csv("cloth$data.csv")

x1=[]
y1=[]
 
for i in frame['Year']:
    x1.append(int(i))
for i in frame['Residential & commercial (tonnes)']:
    y1.append(float(i))
x2=np.array(x1)
y2=np.array(y1)
N=100
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace1 = go.Scatter(
    x = x2,
    y = y2,
    mode = 'markers+lines'
)

trace2 = go.Scatter(
    x = x2,
    y = y2,
    mode = 'markers+lines'
)



# Plot and embed in ipython notebook!


# plot
fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)

fig['layout'].update(height=600, width=800, title='i <3 annotations and subplots')
plot(fig)
#plot(data)




    

