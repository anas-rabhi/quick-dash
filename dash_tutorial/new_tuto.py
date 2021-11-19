import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
data = pd.DataFrame({'a': ['c', 'd'], 'b': [20, 40]})
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            figure=px.bar(data, x='a', y='b'))

    ], style={'width': '48%', 'display': 'inline-block', 'float':'right'}),


    html.Div([
        dcc.RadioItems(
            id='xaxis-aztype',
            options=[{'label': 'i', 'value': 'i'}],
            value='Linear',
            labelStyle={'display': 'inline-block'}
        ),
    dcc.Graph(
                figure=px.bar(data, x='a', y='b'))
    ], style={'width': '100%', 'display': 'inline-block'})
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)