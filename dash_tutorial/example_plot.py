import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px



app = dash.Dash(__name__)

app.layout = html.Div([


####### MID layout
        html.Div([
            dcc.Dropdown(
                id='id_cpam-dropdown',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                value=None,
                multi=True,
            ),
            html.Br(),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                multi=True,
            ),
            html.Br(),
            dcc.Dropdown(
                id='prof-dropdown',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                multi=True,
            ),
            dcc.RadioItems(
                id='choix',
                options=[{'label': 'PS NON STABLE', 'value': 'PS_NS'},
                         {'label': 'PS STABLE', 'value': 'PS_S'},
                         {'label': 'AUCUN', 'value': 'AUCUN'}],
                value='AUCUN',
            )
            ,

        ]),

###################  RIGHT LAYOUT

        html.Div([
            html.Br(),
            dcc.Dropdown(
                id='media2021-dropdown',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                multi=True,
            ),
            dcc.Graph(id='graph-2021'),

            html.Br(),

            dcc.Dropdown(
                id='media2021-dropdown-csp2',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                multi=True,
            ),

            html.Br(),
            dcc.Graph(id='graph-2021-csp2')

        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),




########################################################################################################################

######### left layout
        html.Div([
            html.Br(),
            dcc.Dropdown(
                id='media2020-dropdown',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                multi=True,
            ),
            dcc.Graph(id='graph-2020'),

            html.Br(),
            dcc.Dropdown(
                id='media2021cpam-dropdown',
                options=[{'label': 'EE', 'value': 'c'}
                         ],
                multi=True,
            ),
            dcc.Graph(id='graphcpam-2021'),
            html.Br(),
            dcc.Graph(
                    id='prof'
                )

        ], style={'width': '49%', 'float': 'left', 'display': 'inline-block'})
    ])



if __name__ == '__main__':
    app.run_server(debug=True)