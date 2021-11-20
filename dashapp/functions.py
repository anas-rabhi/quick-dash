import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


filters = {
    'checklist': dcc.Checklist, #    labelStyle={'display': 'inline-block'}
    'alert': dcc.ConfirmDialog,
    'date_range': dcc.DatePickerRange,
    'dropdown': dcc.Dropdown,
    'checkbox': dcc.RadioItems,
    'range_slider': dcc.RangeSlider,
    'slider': dcc.Slider
}

def define_params(type: str, var: str,**params):
    filter = filters[type]
