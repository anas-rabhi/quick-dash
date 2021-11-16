from typing import (Dict,
                    List,
                    Callable)
import dash

class Dashboard:
    def __init__(self, data):

        #n_layout = n_layout
        self.data = data
        self.right = {}
        self.left = {}
        self.mid = {}

    def available(self):
        next = 0

    def add_plot(self, plot: Callable, **params):
        mid = {}

    def add_plot_right(self):
        right = {}

    def add_plot_left(self):
        right = {}

    def run_app(self):
        app = dash.Dash(__name__)
        app.layout()


