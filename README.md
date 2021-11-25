# Quick Dash 

Low-code and quick dash dashboards.

# Installation

```shell
pip install git+https://github.com/anas-rabhi/quick-dash
```
## Getting Started

In this example, I initiate the class, then I plot one graph at the left 
another one at the right then one at the middle. Then start the app.

**Important** : Dash uses plotly for the visualizations. For more information 
visit plotly doc: https://plotly.com/python/

```python
from dashapp import *

data = pd.DataFrame({
    'Brand': ['iPhone', 'OnePlus', 'Pixel'],
    'Price': [9999, 1000, 500],
    'Battery': [500, 502, 520],
    'RAM': [4, 0, 3]})

# The title is empty by default but you can add one
my_app = Dashboard(data, title='My App')

# Once the class is initiated you can add plots into your dashboard :
my_app.add_plot('left', px.bar, id='123', x='Brand', y='Price') # px.bar is the barplot from plotly.

# Add right plot
my_app.add_plot('right', px.bar, id='123', x='Brand', y='Battery') # px.bar is the barplot from plotly.

# Add middle plot
my_app.add_plot('mid', px.bar, id='123', x='Brand', y='Battery') # px.bar is the barplot from plotly.

# Then start the app :
my_app.run_app()

```


