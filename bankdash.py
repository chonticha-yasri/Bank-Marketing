import numpy as np
import pandas as pd

import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

Bank = pd.read_csv('BankETL.csv', sep=',')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

header = html.H2(children="Bank marketing")

#---------------------------------------------------------------------------------------------------------------------------#
chart1 = px.histogram(data_frame=Bank.sort_values('deposit_no'),
           x="poutcome",
           y= ["deposit_yes","deposit_no"],
           color_discrete_sequence=["salmon", "mediumpurple"],
           title="PAST OUTCOMES")


graph1 = dcc.Graph(
        id='graph1',
        figure=chart1,
        className="six columns"
    )

#---------------------------------------------------------------------------------------------------------------------------#

chart2 = px.scatter(Bank, 
            x='age', 
            y='balance',
            color="deposit_yes",
            facet_col="deposit_yes",
            title='AGE VS BALANCE TERM DEPOSIT SUBSCRIPTION')

graph2 = dcc.Graph(
        id='graph2',
        figure=chart2, 
        className="six columns"
    )

#---------------------------------------------------------------------------------------------------------------------------#
chart3 = px.pie(Bank,
            values='deposit_yes', 
            names='job', 
            title='THE MOST JOB IN THE CAMPAIGN')

graph3 = dcc.Graph(
        id='graph3',
        figure=chart3,
        className="six columns"
    )
#---------------------------------------------------------------------------------------------------------------------------#
chart4 = px.histogram(data_frame=Bank.sort_values('deposit_yes'),
           x =["education","marital","contact"],
           y="deposit_yes",
           color_discrete_sequence=["salmon", "mediumpurple",'YellowGreen','Gold'],
           title="PERSONAL INFORMATION TERM DEPOSIT")
           

graph4 = dcc.Graph(
        id='graph4',
        figure=chart4, 
        className="six columns"
    )
#---------------------------------------------------------------------------------------------------------------------------#
chart5 = px.histogram(data_frame=Bank,
            x='duration',
            y =['deposit_yes','deposit_no'],
            title="DURATION TERM DEPOSIT SUBSCRIPTION")

graph5 = dcc.Graph(
        id='graph5',
        figure=chart5,
        className="six columns"
    )
#---------------------------------------------------------------------------------------------------------------------------#
chart6 = px.scatter(Bank, 
            x='campaign', 
            y='duration',
            facet_col="deposit_yes",
            title="DURATION VS CAMPAINGN TERM DEPOSIT SUBSCRIPTION")
            
graph6 = dcc.Graph(
        id='graph6',
        figure=chart6, 
        className="six columns"
    )

#---------------------------------------------------------------------------------------------------------------------------#
chart7 = px.histogram(Bank, 
            x='loan', 
            y='deposit_yes',
            color='loan',
            color_discrete_sequence=["mediumpurple",'YellowGreen'],
            title="LOAN TERM DEPOSIT SUBSCRIPTION")
  
graph7 = dcc.Graph(
        id='graph7',
        figure=chart7, 
        className="six columns"
    )
#---------------------------------------------------------------------------------------------------------------------------#
row2 = html.Div(children=[graph1,graph2],)

row1 = html.Div(children=[graph3,graph4],)

row3 = html.Div(children=[graph5,graph6],)

row4 = html.Div(children=[graph7],)

layout = html.Div(children=[header, row1,row2,row3,row4], style={"text-align": "center"})

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)