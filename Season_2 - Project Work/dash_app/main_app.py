# set path for relative import 
import sys 
from pathlib import Path

from numpy.lib.function_base import _update_dim_sizes
sys.path[0] = str(Path(sys.path[0]).parent)

# import libraries  dash, dcc, html , Input, Output 
import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
from src.model import cl 
from src.code import dl 
import plotly.express as px 
import pandas as pd 

disp_options = dl.cur_options 

# initialise app 
App = dash.Dash(title = "Disease - Predictor")

styles = { 
            'background' : '#111111', 
            'text'   : '#7FDBFF',
            'font-size' : '50px'
        }

App.layout = html.Div(
    [
        html.H2('Disease - Predictor', style = {'textAlign': 'center', 'color': styles['text']} ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.H4('Gender:', style = {'display':'inline'} ),
                        dcc.RadioItems(id='gender',
                            options = [
                                {'label': 'Male', 'value' : 'M'},
                                {'label': 'Female', 'value' : 'F'},
                                {'label': 'Prefer not to say', 'value' : 'O'}
                            ],
                            style= {'display':'inline'}

                        ),
                        
                    ],

                ),

                html.Div(
                    [
                        html.H4('Age(5-99):'),
                        dcc.Input(type = 'number', min = 5, max = 99),
                    ], 
                    style = {'columnCount': 2, 'width': '50%'}
                ),
                
            ], style = {'columnCount': 2, 'margin':'15px'}
        ),
        html.Div(
            [
                html.H4('Select Symptoms :-'),
                dcc.Checklist(
                    options = disp_options ,
                    labelStyle = {'display': 'block', 'margin':'10px'},
                    id = 'disp-options',
                    value = []      
                ),
            ], 
            style = {'height':'330px'}
        ),
        html.Hr() ,
                html.Button('Next',id='next-button',n_clicks=0, 
                           style={'height':'30px','width':'70px'}),
        dcc.Graph(id='bar-graph' ,figure=dl.fig)
    ],
)

@App.callback(
        Output(component_id='disp-options',component_property='options'),
        Output(component_id='next-button', component_property='n_clicks'),
        Output(component_id='bar-graph',component_property='figure'),
        Input(component_id='disp-options',component_property='options'),
        Input(component_id='disp-options',component_property='value'),
        Input(component_id='next-button', component_property='n_clicks'),
        Input(component_id='bar-graph',component_property='figure'),

        prevent_initial_call = True 
)
def callback_function_1(options,selected_options,n_clicks,figure):
        print(len(dl.rem_options))
        print(selected_options)
        if (n_clicks): 
                options = dl.update_options(selected_options)
                n_clicks = 0 
        if (len(selected_options)>0) : 
                predictions = cl.predict(selected_options)
                dl.fig['data'][0]['x'] = list(predictions.loc[:,'Disease'])
                dl.fig['data'][0]['y'] = list(predictions.loc[:,'Prob'])
                figure = dl.fig
        else : 
                dl.fig['data'][0]['x'] = []
                dl.fig['data'][0]['y'] = []
                figure = dl.fig
  

        return options,n_clicks,figure 


@App.callback(
    Output(component_id='gender',component_property='value'),
    Input(component_id='gender',component_property='value')
)
def callback_function_2(gender) : 
    if (gender == None) : 
        dash.exceptions.PreventUpdate
    if (gender == 'M') :
        dl.rem_options = [col for col in dl.rem_options if col not in dl.female_symp ]
    return gender 

App.run_server(debug=True)