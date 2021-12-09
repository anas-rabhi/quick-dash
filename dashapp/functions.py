import dash
from dash import dcc, html
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

######## ADD checkbox & radioitems
######## text box output

def show():
    print(filters)

def define_params(data: pd.DataFrame, ftype: str, var: str, id: str, **params):
    displayed = filters[ftype]

    param = {}

    if type in ['slider', 'range_slider']:

        if 'value' not in params:
            params['value'] = [data[var].min(),
                               data[var].max()]

        param['id'] = id
        param['min'] = data[var].min()
        param['max'] = data[var].max()
        param['step'] = 0.5 #to change

        return displayed(**param, **params)

    if ftype in ['dropdown']:

        if 'value' not in params:
            params['value'] = None

        param['options'] = [{'label': i, 'value': i} for i in data[var].unique().tolist()]
        param['id'] = id

        return displayed(**param, **params)

    if type in ['date_range']:

        param['id'] = id
        param['min_date_allowed'] = data[var].min()
        param['max_date_allowed'] = data[var].min()
        param['initial_visible_month'] = data[var].min()

        return displayed(**param, **params)


#data = pd.DataFrame({'a': ['c', 'd'], 'b': [20, 40]})
#define_params(data, 'checklist', 'a', '555a')