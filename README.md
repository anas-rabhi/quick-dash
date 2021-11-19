# Quick Dash 

The purpose of this work is to build quick dash dashboards
without writing all the dash "html" code and without having
to organize the visualizations. 
The dashboard will be also deployable
pretty easy on Docker, in order to be able to share it externally.
My first motivation is of course save time and be able to 
share the dashboard online.


# Installation

```shell
git .....
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
my_app.add_plot('right', px.scatter, id='123', x='Battery', y='Battery', color='Brand') # px.bar is the barplot from plotly.

# Then start the app :

```


### Adding dropdowns

### Adding interaction between dropdowns and graphs
