import pandas as pd
import plotly.figure_factory as pff

fil= pd.read_csv('csvs/8.csv')

grapq= pff.create_distplot([fil['Avg Rating'].tolist()],['name'],show_hist=False)
grapq.show()