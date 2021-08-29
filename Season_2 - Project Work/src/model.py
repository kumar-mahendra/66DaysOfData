from sklearn import tree 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import numpy as np 
le = LabelEncoder()
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier

class Model : 
    def __init__(self): 
        self.columns = [] 
        self.Xshape = None
        self.model = None 
        self.X_train = None 
        self.X_test = None 
        self.y_train = None 
        self.y_test = None 
        self.accuracy = None

    def prepare_dataset(self): 
        # import data 
        train_data = pd.read_excel('data/diseases_with_symptoms.xlsx')
        test_data = pd.read_excel('data/diseases_with_symptoms.xlsx')

        self.y_train = train_data.loc[:,['Diseases']]
        self.y_train = np.array(self.y_train).reshape(-1)

        self.y_test = test_data.loc[:,['Diseases']]
        self.y_test = np.array(self.y_test).reshape(-1)

        self.X_train = train_data.drop('Diseases', axis = 1)
        self.X_test = test_data.drop('Diseases', axis = 1)

        self.columns = self.X_train.columns 
        self.Xshape = np.shape(self.columns) 

        return self.X_train,self.X_test,self.y_train,self.y_test


    def define_model(self,n_estimators): 
        self.model = RandomForestClassifier(n_estimators=n_estimators)
        return self.model 

    def encoding_labels(self): 
        self.y_train_le = le.fit_transform(self.y_train)
        self.y_train_le = pd.DataFrame(self.y_train_le, columns = ['Diseases'])
        self.y_test_le = le.transform(self.y_test)
        # return self.y_train_le, self.y_test_le

    def train_and_predict_model(self):
        self.encoding_labels()
        self.y_train_le = np.array(self.y_train_le).reshape(-1)
        self.model.fit(self.X_train,self.y_train_le)
        y_pred = self.model.predict(self.X_train)
        temp_y = self.y_train_le
        self.accuracy = ((y_pred == temp_y).sum())
        return y_pred, self.accuracy

    def predict_new_X_test(self,X_selected_cols):
        empty_row = np.zeros(self.Xshape)
        X_new = pd.DataFrame(data=empty_row,columns=self.columns)
        for col in X_selected_cols :
            X_new.loc[0,col] = 1 
        pred_y = self.model.predict(X_new) 
        return pred_y 

class_Model = Model()
class_Model.prepare_dataset()
class_Model.define_model(10)
_ , acc = class_Model.train_and_predict_model()
print("total : ",len(_))
print("Accuracy : ",acc)