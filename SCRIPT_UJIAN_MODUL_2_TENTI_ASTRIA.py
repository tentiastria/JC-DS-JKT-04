import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dfUjian = pd.read_csv('tsa_claims_ujian.csv')

app.layout = html.Div(children = [
    dcc.Tabs(value = 'tabs', id = 'tabs', children = [
        dcc.Tab(label = 'DataTable', children = [
            html.Div(children = [
                                            html.P('Claim Site : '),
                                            dcc.Dropdown(id = 'dropdown',
                                                        options = [{'label' : i, 'value' : i} for i in dfUjian['Claim Site'].unique()],
                                                        value = 'All')
                                        ],
                                        className = 'col-4'),
                    html.Div(children = [
                                            html.P('Max Row :'),
                                            dcc.Input(id='max-row', type='number', min = 5, max = 20, value = 10),
                                                        # options = [{'label' : n, 'value' : n} for n in [1,5,10,20]],
                                                        # value = 5),

                                            html.Div(html.Button('Search', id = 'Search'), className ='col-4'),

                                            html.Div(dash_table.DataTable(id='table',
                                                                    columns=[{"name": i, 'id' : i} for i in dfUjian.columns],
                                                                    data=dfUjian.to_dict('records'),
                                                                    page_action = 'native',
                                                                    page_current = 0,
                                                                    page_size = 10))
                                        ])]),
        dcc.Tab(label = 'Graph Bar', children = [
                    html.Div(children = [
                        html.Div(children = [
                            html.P('X1 : '),
                            dcc.Dropdown(id = 'x-axis-1',
                                        options = [{'label' : i, 'value' : i} for i in dfUjian.select_dtypes('number').columns],
                                        value = 'Claim Amount')],
                                        className = 'col-4'),
                        html.Div(children = [
                            html.P('X2 :'),
                            dcc.Dropdown(id = 'x-axis-2',
                                        options = [{'label' : i, 'value' : i } for i in dfUjian.select_dtypes('number').columns],
                                        value = 'Close Amount')],
                            className = 'col-4')],
                            className = 'row'),

                        html.Div([
                                    ## Graph Bar
                                dcc.Graph(
                                id ='contoh-graph-bar',
                                figure = {
                                            'data' : [
                                                        {{'x' : (dfUjian['survived'].drop_duplicates().sort_values()), 'y' : (dfUjian[dfUjian['pclass'] == 1]['survived'].value_counts(), 'type' : 'bar', 'name' : 'Attack' },
                                                        {'x' : dfUjian['Close Amount'], 'y' :dfUjian['Speed'], 'type' : 'bar', 'name' : 'speed'}
                                                    ],
                                                'layout' : {'title' : 'Dashboard Pokemon Attack'}
                                        }
                                        )], className = 'col-12')
                    ]),

        dcc.Tab()
        ],
        content_style = {
        'fontFamily' : 'Arial',
        'borderBottom' : '1px solid #d6d6d6',
        'borderLeft' : '1px solid #d6d6d6',
        'borderRight' : '1px solid #d6d6d6',
        'padding' : '44px'})
    ],
    style = {
    'maxWidth' : '1200px',
    'margin' : '0 auto'})

@app.callback(
    Output(component_id='table' , component_property=''),
    [Input(component_id ='Search', component_property='n_clicks'),
    Input(component_id='dropdown', component_property='value'),
    Input(component_id ='max-row',component_property= 'value')])
def update_output(n_clicks, value):
    data = dfUjian.to_dict('records')
    return data

@app.callback(
    Output(component_id='contoh-graph-bar', component_property='figure'),
    [Input(component_id='x-axis-1', component_property='value'),
    Input(component_id='x-axis-2', component_property='value')]
)
def create_graph_bar(x1,x2):
    figure = {
                                    'data' : [
                                                {'x' : dfUjian['Generation'], 'y' :dfUjian[x1], 'type' : 'bar', 'name' : 'x1'},
                                                {'x' : dfUjian['Generation'], 'y' :dfUjian[x2], 'type' : 'bar', 'name' : 'x2'}
                                            ],
                                    'layout' : {'title' : 'Bar Chart'}
                                }
    return figure



if __name__ == '__main__':
    app.run_server(debug=True)