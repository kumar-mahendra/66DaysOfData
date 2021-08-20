
# Make required imports 

import dash
import plotly.express as px 
import dash_core_components as dcc 
import dash_html_components as html
import pandas as pd 
from dash.dependencies import Input, Output 


my_app = dash.Dash()


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
                                                html.H4('Gender :'), 
                                                dcc.RadioItems(
                                                        options = [
                                                                {'label' : 'Male', 'value' : 'M' } , 
                                                                {'label' : 'Female', 'value': 'F'}, 
                                                        ]
                                                ),
                                        ], style = {'columnCount':3, 'float':'left'}
                                ),

                                html.Div(
                                        [
                                                html.H4('Age :'), 
                                                dcc.Input(id='age',placeholder='Enter your age here',type='number'),
                                        ], style = {'columnCount':2, 'width': '50%'}
                                ),

                ], style = {'columnCount': 2}
                ),

                html.Hr(),

                html.Div(
                        [    
                                html.H3('Select your symptoms :-'),  
                                dcc.Checklist(
                                        options = [
                                                {'label': 'Symptom 1', 'value': 'Symptom 1'},
                                                {'label': 'Symptom 2', 'value': 'Symptom 2'},
                                                {'label': 'Symptom 3', 'value': 'Symptom 3'}
                                        ],
                                        id = 'selected-boxes',
                                ),
                        ]
                )
       ], 
)

@my_app.callback(

        Output(component_id='selected-boxes', component_property='options'),
        Input(component_id='selected-boxes', component_property='options'),
        Input(component_id='selected-boxes',component_property='value')

)
def print_output(options , selected_values): 
        
        new_options = []
        if (options is None) : 
                raise dash.exceptions.PreventUpdate 
        if (selected_values is None) : 
                raise dash.exceptions.PreventUpdate

        trash = []
        for label_value in options : 
                label, value = label_value['label'], label_value['value']
                if (value not in selected_values) : 
                        new_options.append({'label':label, 'value':value})
                else : 
                        trash.append({'label':label, 'value':value})
        
        return new_options 
        
my_app.run_server(debug=True)

