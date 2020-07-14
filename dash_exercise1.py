import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 
import numpy as np 
import pandas as pd




app = dash.Dash()

df = pd.read_csv('data/OldFaithful.csv')

print(df.head())

app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = {'data': [
                        go.Scatter(
                            x=df['X'],
                            y=df['Y'],
                            hovertext=df['D'],
                            mode='markers',
                            marker= {
                                'size':5,
                                'color':'rgb(0,0,255)',
                                'line':{'width':2}
                            }
                        )],
                        'layout':go.Layout(title='Old Faithful eurption intervals',xaxis = {'title':'magnitude'}, yaxis={'title':'interval to next (minutes)'})}
                    )])



if __name__ == '__main__':
    app.run_server()