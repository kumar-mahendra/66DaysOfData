# import required libraries 
import pandas as pd 
import numpy as np 


dir = 'data/train_data.csv'


data = pd.read_csv(dir)
data.drop('Unnamed: 0', axis=1, inplace=True)

all_symptoms = [ col for col in data.columns if col not in ['prognosis'] ]

disease_symptoms_dict = {}
for i, disease in enumerate(data['prognosis']) : 
    cur_symptoms = [  col for col in all_symptoms if data.loc[i, col]==1 ]
    if disease not in disease_symptoms_dict : 
        disease_symptoms_dict[ disease ] = []   

    disease_symptoms_dict[disease].extend(cur_symptoms)
    disease_symptoms_dict[disease] = list(set(disease_symptoms_dict[disease]))

n_diseases = len(disease_symptoms_dict)
n_symptoms  = len(all_symptoms)

# print(n_diseases, n_symptoms)
# print(disease_symptoms_dict.keys())

new_data = np.zeros((n_diseases, n_symptoms+1), dtype = int)
new_data = pd.DataFrame( new_data, columns=all_symptoms + ['Disease'] ) 

i = 0 
for disease, symptoms  in disease_symptoms_dict.items() : 
    
    new_data.loc[i,'Disease'] = disease
    for col in symptoms : 
        new_data.loc[i,col] = 1 

    i += 1 

# print(new_data.head())
# print(new_data.shape)

# Save new_data to csv file "train2_modified.csv"

new_data.to_csv('data/train2_modified.csv')







