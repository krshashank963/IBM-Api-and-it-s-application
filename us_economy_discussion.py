# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 07:59:08 2020

@author: SHASHANK RAJPUT
"""


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

a= (pd.read_csv(links['GDP']))
pd.DataFrame(a)
a.head()    

b =pd.read_csv(links['unemployment'])
pd.DataFrame(b)
b.head()

df=pd.read_csv(links['unemployment'])
df1=df[df['unemployment']>8.5]
df1

gdp=pd.read_csv(links['GDP'])
x = pd.DataFrame(gdp, columns=['date'])
x.head()

gdp_change = a[['change-current']]
pd.DataFrame(gdp_change)

unemployment = b[['unemployment']]
pd.DataFrame(unemployment)

title = 'my_string'
file_name = "index.html"
make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title='my_string', file_name='index.html')


