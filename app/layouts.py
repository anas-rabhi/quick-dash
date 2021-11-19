from typing import (Dict,
                    List,
                    Callable,
                    Literal,
                    )
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


class Dashboard:

    # dataframe or dictionnary ? add bellow
    def __init__(self, data: pd.DataFrame):
        if isinstance(data, pd.DataFrame):
            pass
        else:
            raise AttributeError("The data must be a Dataframe object, at least for now...")


        # n_layout = n_layout
        self.data = data
        self.layout = []
        self.mid_layout = []
        self.right_layout = []
        self.left_layout = []
        self.figures = {}
        self.all_layouts = []
        self.all_ids = []

    # show current figures --> jupyter, plot all
    def show(self):
        i = 2

    def available(self):
        next = 0  # coming soon...

        # self.mid_layout.append(html.Br())

    def add_plot(self, where: str, plot: Callable, id: str, **params):

        if id in self.all_ids:
            raise AttributeError("the ID is already taken, please choose another one")

        if where not in ['mid', 'right', 'left']:
            raise AttributeError("where parameter should be equal to mid, left or right")

        self.all_ids.append(id)

        fig = plot(self.data, **params)
        self.figures[id] = fig

        graph = dcc.Graph(
            id=id,
            figure=self.figures[id])

        if where == 'mid':

            self.mid_layout.append(graph)
            self._close_past_layouts(mid=self.mid_layout)

        if where == 'left':

            self.left_layout.append(graph)
            self._close_past_layouts(left=self.left_layout)

        if where == 'right':

            self.right_layout.append(graph)
            self._close_past_layouts(right=self.right_layout)

    def close_current(self):
        self._close_past_layouts(mid=self.layout, left=self.left_layout, right=self.right_layout)

    def add_plot_right(self, plot: Callable, **params):
        if id in self.all_ids:
            raise AttributeError("the ID is already taken, please choose another one")

        self._close_past_layouts(left=self.left_layout, mid=self.mid_layout)
        fig = plot(self.data, **params)
        self.figures[id] = fig

        graph = dcc.Graph(
            id=id,
            figure=self.figures[id])

        self.all_ids.append(id)
        self.right_layout.append(graph)

        # self.mid_layout.append(html.Br())

    def add_plot_left(self, plot: Callable, **params):
        # left = {}
        self._close_past_layouts(mid=self.mid_layout, right=self.right_layout)

    def add_inter(self, output: List = [], input: List = []):
        add = 0

    def run_app(self, port: int = 8050):

        print('ok')
        app = dash.Dash(__name__)
        print('ok')
        app.layout = html.Div(self.layout)
        app.run_server(debug=True, port=port)

    def _close_past_layouts(self, **kwargs):

        for i in kwargs:
            if (i == 'mid') & (len(kwargs[i]) != 0):
                self.layout.append(self._close_div(self.mid_layout, where='mid'))
                self.mid_layout = []

            if (i == 'left') & (len(kwargs[i]) != 0):
                self.layout.append(self._close_div(self.left_layout, where='left'))
                self.left_layout = []

            if (i == 'right') & (len(kwargs[i]) != 0):
                self.layout.append(self._close_div(self.right_layout, where='right'))
                self.right_layout = []

    # this function would be useful later when dropdowns are added
    def _close_div(self, x: List, where: str):

        if where not in ['mid', 'right', 'left']:
            raise AttributeError("where parameter should be equal to mid, left or right")

        if where == 'mid':
            return html.Div(x, style={'width': '100%', 'display': 'inline-block'})

        if where == 'left':
            return html.Div(x, style={'width': '49%', 'display': 'inline-block'})

        if where == 'right':
            return html.Div(x, style={'width': '49%', 'float': 'right', 'display': 'inline-block'})

    # function to optimize with the top one
