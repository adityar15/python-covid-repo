import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

## Creating the graphs
covid = pd.read_csv("cases_country_month.csv")
conf_line = px.line(data_frame=covid, x = 'Year-Month', y = 'Confirmed',
    title = 'Confirmed Cases by Month')
deaths_line = px.line(data_frame=covid, x = 'Year-Month', y = 'Deaths',
    title = 'Death Cases by Month')
recov_line = px.line(data_frame=covid, x = 'Year-Month', y = 'Recovered',
    title = 'Recovered Cases by Month')

## Web App Contents
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    # Title
    html.H1(' COVID Cases Time Series'),
    # Confirmed Case Line Graph
    html.Div(dcc.Graph(id = 'conf_line', figure = conf_line)),
    # Death Case Line Graph
    html.Div(dcc.Graph(id = 'deaths_line', figure = deaths_line)),
    # Recovered Case Line Graph
    html.Div(dcc.Graph(id = 'recov_line', figure = recov_line)),
    # Creating Dropdown
    html.Div([dcc.Dropdown(
        id = 'dropdown',
        options = [
            {'label': 'Afghanistan', 'value': 'Afghanistan'}
        ],
        placeholder = "Select a city",
        multi=True
    ),
    html.Div(id = 'dd-output-container')
    ])
])

# Part of Dropdown
@app.callback(
    Output('dd-output-container', 'children'),
    Input('dropdown', 'value')
)
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)

