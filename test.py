from dashapp import *
import pandas as pd
# add some data

data = pd.DataFrame({
    'Brand': ['iPhone', 'OnePlus', 'Pixel', 'Poco', 'Samsung'],
    'Price': [2040, 1000, 500, 450, 2000],
    'Battery': [500, 502, 520, 550, 530],
    'RAM': [4, 1, 3, 5, 6],
    'Rating': [70, 80, 90, 85, 70],
    'Design': ['Nice', 'Horrible', 'Neutral', 'Nice', 'Horrible']})

# initiating the dashboard class with the data as a parameter
new = Dashboard(data, title='Demo APP')

# adding one left plot
new.add_filter(where='mid', ftype='dropdown', var='Brand', id='top_dropdown', multi=True)
new.add_filter(where='mid', ftype='dropdown', var='Design', id='top_dropdown_2', multi=True)


new.add_plot(where='mid', plot=px.bar, id='mid_plot', x='Brand', y='Price', color="Battery", title='Phone prices')

# adding one right plot
new.add_plot(where='right', plot=px.bar, id='right_plot', x='Brand', y='Battery', title='Phone battery')
new.add_plot(where='left', plot=px.bar, id='left_plot', x='Brand', y='RAM', title='Phone RAM')

new.add_plot(where='mid', plot=px.bar, id='mid_plot_2', x='Brand', y='Rating', color='Price', title='Phone Rating')

new.add_callback(input_id=['top_dropdown', 'top_dropdown_2'], output_id=['mid_plot', 'left_plot', 'right_plot', 'mid_plot_2'])
#new.add_callback(input_id=['top_dropdown_2'], output_id=['mid_plot', 'left_plot', 'right_plot', 'mid_plot_2'])

#new.add_callback(input_id=['top_dropdown'], output_id=['right_plot'])
#new.add_callback(input_id=['top_dropdown'], output_id=['left_plot'])
#new.add_callback(input_id=['top_dropdown'], output_id=['mid_plot_2'])
#new.get_info()


if __name__ == '__main__':
    new.run_app()
