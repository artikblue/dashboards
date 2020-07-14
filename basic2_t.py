import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 
import numpy as np 
import requests, json
import pandas as pd



url = "http://127.0.0.1:5001/offer"

r = requests.get(url=url)

rj = r.json()
rj = json.loads(rj)

df = pd.DataFrame(rj)
df["feats"]=df["feats"].apply(lambda x: len(x))
df["images"]=df["images"].apply(lambda x: len(x))

print(df.head())


#df2 = pd.DataFrame({'percentage': df.groupby(['company'] ,as_index=False).size() / len(df) }).reset_index()

#df2 = pd.DataFrame({'percentage': df.groupby([ 'site']).size() / len(df)}).reset_index()
#df2 = df.groupby('zone').count().reset_index()
#print(df2.head())

app = dash.Dash()



app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Box(
                            y=df[df.site=='pisoscom']['price'],
                            name="pisos.com"
                            
                            
                             
                        ),
                        go.Box(
                            y=df[df.site=='habitaclia']['price'],
                            name="habitaclia"
                            
                            
                             
                        )],
                        'layout':go.Layout(title='Price/Surface', xaxis={'title':'price distribution'}, yaxis={'title':'surface'})})])


"""
app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Box(
                            y=df[df.site=='pisoscom']['price'],
                            name="pisos.com"
                            
                            
                             
                        ),
                        go.Box(
                            y=df[df.site=='habitaclia']['price'],
                            name="habitaclia"
                            
                            
                             
                        )],
                        'layout':go.Layout(title='Price/Surface', xaxis={'title':'price distribution'}, yaxis={'title':'surface'})})])


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Scatter(
                             x=df['price'],
                             y=df['surface'],
                             text=df['address'],
                             mode='markers',
                             marker=dict( color=df['city'])
                             
                        )],
                        'layout':go.Layout(title='Price/Surface', xaxis={'title':'price'}, yaxis={'title':'surface'})})])


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Bar(
                             y=df2['zone'],
                             x=df2['_id'],
                             orientation='h'
                        )],
                        'layout':go.Layout(title='Offers per Zone')})])

app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Histogram(
                             x=df['surface']
                        )],
                        'layout':go.Layout(title='Surface histogram (m2)')})])


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Scatter(
                             x=df['price'],
                             y=df['surface'],
                             mode='markers'
                        )],
                        'layout':go.Layout(title='Price/Surface', xaxis={'title':'price'}, yaxis={'title':'surface'})})])


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Histogram(
                             x=df['price']
                        )],
                        'layout':go.Layout(title='Price histogram')})])


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Pie(
                             values=df2['percentage'],labels=df2['site']
                        )],
                        'layout':go.Layout(title='Offers per site')})])


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Bar(
                            x=df2['company'],
                            y=df2['percentage']
                        )],
                        'layout':go.Layout(title='My bar plot',xaxis = {'title':'some x title'})})])

"""
if __name__ == '__main__':
    app.run_server()