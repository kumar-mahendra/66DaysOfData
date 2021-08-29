import numpy as np 
import pandas as pd 

Options = {}

def get_options(selected_options=[]):
    global Options 
    Options = update_Options(selected_options,Options) 
    # function to predict disease 
    new_options = [ {'label' : description, 'value': short_id} for short_id,description in Options.items() ]
    return new_options     

def update_Options(selected_options,Options):
    
    global tmp , col_description 

    new_selected_cols = [] 

    # case-1 : No option selected 
    if (len(selected_options) == 0 ):
        tmp = [col for col in tmp if col not in Options]
        new_selected_cols = tmp[:10]

    # case - 2 : some options selected
    elif(len(selected_options)>0):
        tmp = [col for col in tmp if col not in Options]
        tmp_data = data[data[selected_options].sum(axis=1)>0][tmp]
        tmp_cols = tmp_data.sum(axis=0)
        tmp_cols = tmp_cols[tmp_cols>0]
        tmp_cols = tmp_cols.sort_values(ascending=False)
        new_selected_cols = tmp_cols.index[:10]
        # print(selected_symptoms)

    description_new_selected_cols = [col_description[col] for col in new_selected_cols]
    new_options = {label:value for label,value in zip(new_selected_cols,description_new_selected_cols)}
    return new_options 

PATH = 'data/diseases_with_symptoms.xlsx'
data = pd.read_excel(PATH)
data2 = pd.read_excel(PATH,sheet_name='Final_Symptoms')

columns = [col for col in data.columns if col !='Diseases']
col_description = { col : list(data2[data2['Code']==col]['Description'])[0] for col in columns } 


freq_counts = { col : data[col].sum() for col in columns}
freq_counts = {k: v for k,v in sorted(freq_counts.items(), key= lambda item : -item[1]) }
freq_counts_keys = list(freq_counts.keys())

selected_cols = np.random.choice(freq_counts_keys[:20],10, replace=False)
description_selected_cols = [col_description[col] for col in selected_cols]
Options = {label:value for label,value in zip(selected_cols,description_selected_cols)}

tmp = freq_counts_keys 
