# set path for relative import 
import sys 
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

# Make required imports 
import dash
import plotly.express as px 
import dash_core_components as dcc 
import dash_html_components as html
import pandas as pd 
from dash.dependencies import Input, Output 
from src.code import get_options 


class OutputData : 
        def __init__(self) :
                self.selected_so_far = []      

output = OutputData()

my_app = dash.Dash(title="Pre-doctor inspection")

colors = { 'background' : '#111111', 
            'text'   : '#7FDBFF'
         }

my_app.layout = html.Div(
        children = [
                html.H2('Pre-Doctor Inspection', style={'textAlign': 'center','color': colors['text']}   ),   
                html.Hr(),               
                html.Div( 
                children = [
                                html.Div(
                                        [ 
                                                html.H4('Gender :', style= {'display':'inline'}), 
                                                dcc.RadioItems(
                                                        options = [
                                                                {'label' : 'Male', 'value' : 'M' } , 
                                                                {'label' : 'Female', 'value': 'F'}, 
                                                        ],
                                                        style= {'display':'inline'}
                                                       
                                                ),
                                        ],
                                ),

                                html.Div(
                                        [
                                                html.H4('Enter age ( 5 - 99 ): '), 
                                                dcc.Input(type='number',min=5,max=99),
                                        ], style = {'columnCount':2, 'width': '50%'}
                                ),

                ], style = {'columnCount': 2}
                ),

                html.Hr(),

                html.Div(
                        [    
                                html.H3('Select your symptoms :-'),  
                                dcc.Checklist(
                                        options = get_options(),
                                        labelStyle = {'display': 'block', 'margin':'10px'},
                                        id = 'selected-boxes',
                                ),
                        ], style = {'height':'330px'}
                ), 
                html.Hr() ,
                html.Button('More',id='next-button',n_clicks=0, 
                           style={'height':'30px','width':'70px'}),

       ], 
)

@my_app.callback(

        Output(component_id='selected-boxes', component_property='options'),
        Output(component_id='selected-boxes', component_property='value'),
        Output(component_id='next-button',component_property='n_clicks'),
        Input(component_id='selected-boxes', component_property='options'),
        Input(component_id='selected-boxes',component_property='value'),
        Input(component_id='next-button',component_property='n_clicks'),

)
def callback(cur_options , selected_values, n_clicks): 
        
        new_options = []
        if (cur_options is None) : 
                raise dash.exceptions.PreventUpdate 
        if (selected_values is None) : 
                raise dash.exceptions.PreventUpdate

        trash = []
        for label_value in cur_options : 
                label, value = label_value['label'], label_value['value']
                if (value not in selected_values) : 
                        new_options.append({'label':label, 'value':value})
                else : 
                        trash.append( {'label':label, 'value':value} )
        
        if (n_clicks):
                global output 
                new_options = get_options(selected_values)
                if (len(selected_values)>0): 
                        output.selected_so_far.extend(selected_values)
                        print(output.selected_so_far)
                        selected_values = [] 
                n_clicks = 0 

        return new_options, selected_values, n_clicks

my_app.run_server(debug=True)

