from dashapp import *

# add some data
data = pd.DataFrame({'a': ['c', 'd'], 'b': [20, 40]})

# initiating the dashboard class with the data as a parameter
new = Dashboard(data)

# adding one left plot
new.add_plot(where='right', plot=px.bar, id='3', x='a', y='b')
new.add_plot(where='mid', plot=px.bar, id='5d6', x='a', y='b')

# adding one right plot
new.add_plot(where='right', plot=px.bar, id='45', x='a', y='b')
new.add_plot(where='left', plot=px.bar, id='45d', x='a', y='b')
new.add_plot(where='left', plot=px.bar, id='4s5d', x='a', y='b')

new.add_plot(where='mid', plot=px.bar, id='56', x='a', y='b')

new.run_app()