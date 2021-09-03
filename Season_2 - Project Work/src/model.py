import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle 

class Model :
    def __init__(self):
        self.model = pickle.load(open('data/model2.sav','rb')) 
        train_data = pd.read_csv('data/train_data.csv')
        self.X_train = train_data.drop('Diseases', axis = 1)
        self.y_train = train_data.loc[:,['Diseases']]
        self.le = LabelEncoder()
        self.le.fit(self.y_train)

    def predict(self,selected_cols=[]):
        if (len(selected_cols)>0) : 
            n = len(self.X_train.columns)
            symptoms = self.X_train.columns
            X = pd.DataFrame(np.zeros((1,n)), columns = symptoms)
            for col in selected_cols : 
                X.loc[0,col] = 1 
            res = [[indx,prob] for indx,prob  in enumerate(self.model.predict_proba(X).reshape(-1)) ]
            res = sorted(res,key=lambda x : -x[1])
            res = res[:5]
            for i in range(5) : 
                res[i][0] = self.le.inverse_transform([res[i][0]])[0]    
            res = pd.DataFrame(res,columns=['Disease','Prob'])
            return res 
        
cl = Model()   

