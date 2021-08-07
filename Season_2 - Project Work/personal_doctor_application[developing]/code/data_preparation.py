import pandas as pd 
import numpy as np 
data = pd.read_excel('diseases.xlsx')

print(data.head())

dictionary = {}   # to store { disease : list of symptoms }  pairs 
All_symptoms = []
for i in range(len(data)) : 
    if str(data.loc[i,'Disease']) != 'nan':   # check if " disease_name "  changed 
        disease_name = str(data.loc[i,'Disease']).split('_')[-1]
        if (disease_name not in dictionary) : 
            dictionary[disease_name] = []
    symptoms = str(data.loc[i,'Symptom']).split('^')   
    for symptom in symptoms : 
        add = str(symptom.split('_')[-1])
        if (add != 'nan') :   # to ensure symptom is not NaN
            dictionary[disease_name].append(add)


for key,values in dictionary.items() : 
    symptoms = []
    for symptom in values :   
        symptoms.append(  '_'.join(symptom.split(' '))  )
    # print (f'Disease : {key} \t\t Symptoms : {value}')
    All_symptoms.extend(symptoms)

print(len(All_symptoms))
All_symptoms = list(set(All_symptoms))
print('Unique Symptoms : ',len(All_symptoms))
All_symptoms.sort()
# print(*All_symptoms,sep='\n')

data2 = np.zeros((len(dictionary),len(All_symptoms)),dtype="int")
df  = pd.DataFrame(data2,columns=All_symptoms)

print(*df.columns,sep='\n')

# print(len(df),df.shape)
# print(df.head())

# df.to_excel('diseseas_updated.xlsx')
