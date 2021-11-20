import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from typing import Dict, List, Callable
import pandas as pd

filters = {
    'checklist': dcc.Checklist, #    labelStyle={'display': 'inline-block'}
    'alert': dcc.ConfirmDialog,
    'date_range': dcc.DatePickerRange,
    'dropdown': dcc.Dropdown,
    'checkbox': dcc.RadioItems,
    'range_slider': dcc.RangeSlider,
    'slider': dcc.Slider
}


def define_params(data: pd.DataFrame, ftype: str, var: str, id: str, **params):
    displayed = filters[ftype]

    param = {}

    if type in ['slider', 'range_slider']:
        pass

    if ftype in ['checkbox', 'checklist', 'dropdown']:

        if 'value' in params:
            param['value'] = params['value']
        else:
            params['value'] = None

        param['options'] = [{'label': i, 'value': i} for i in data[var].tolist()]
        param['id'] = id

        return displayed(**param, **params)

    if type in ['slider', 'range_slider']:
        pass

#data = pd.DataFrame({'a': ['c', 'd'], 'b': [20, 40]})
#define_params(data, 'checklist', 'a', '555a')