import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
data = pd.DataFrame({'a': ['c', 'd'], 'b': [20, 40]})

app = dash.Dash(__name__)

app.layout = html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    figure=px.bar(data, x='a', y='b')
                )
            ], style={'width': '49%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(
                    figure=px.bar(data, x='a', y='b')
                )
            ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})],

        ),




app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),
    dcc.Graph(
        figure=px.bar(data, x='a', y='b'))

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)