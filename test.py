from dashapp import *
import pandas as pd
# add some data

data = pd.DataFrame({
    'Brand': ['iPhone', 'OnePlus', 'Pixel', 'Poco', 'Samsung'],
    'Price': [2040, 1000, 500, 450, 2000],
    'Battery': [500, 502, 520, 550, 530],
    'RAM': [4, 0, 3, 5, 6],
    'Rating': [70, 80, 90, 85, 70]})

# initiating the dashboard class with the data as a parameter
new = Dashboard(data)

# adding one left plot
new.add_filter(where='mid', ftype='dropdown', var='Brand', id='top_dropdown')
new.add_plot(where='mid', plot=px.bar, id='mid_plot', x='Brand', y='Price')

# adding one right plot
new.add_plot(where='right', plot=px.bar, id='right_plot', x='Brand', y='Battery')
new.add_plot(where='left', plot=px.bar, id='left_plot', x='Brand', y='RAM')

new.add_plot(where='mid', plot=px.bar, id='mid_plot_2', x='Brand', y='Rating')

# to do :
#new.add_callback(input_id=['top_dropdown'], output_id=['mid_plot', 'right_plot', 'left_plot'])

new.add_callback(input_id=['top_dropdown'], output_id=['mid_plot'])
new.add_callback(input_id=['top_dropdown'], output_id=['right_plot'])
new.add_callback(input_id=['top_dropdown'], output_id=['left_plot'])
new.add_callback(input_id=['top_dropdown'], output_id=['mid_plot_2'])


new.run_app()