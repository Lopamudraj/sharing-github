#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.express as px

fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)


# In[ ]:


fig.show()


# In[ ]:


import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

fig = px.line(
    x=["a","b","c"], y=[1,3,2], 
    title="sample figure", height=325
)
fig.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
    html.Pre(
        id='structure',
        style={
            'border': 'thin lightgrey solid', 
            'overflowY': 'scroll',
            'height': '275px'
        }
    )
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


# In[ ]:


get_ipython().system(' pip install plotly')


# In[10]:


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species" , marginal_y="violin",
           marginal_x="box", trendline="ols",template="simple_white")
fig.show()


# In[ ]:


pip install dash


# In[ ]:




