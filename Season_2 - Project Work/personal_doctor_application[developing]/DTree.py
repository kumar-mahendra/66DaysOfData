from sklearn import tree 
import pandas as pd
from sklearn import preprocessing 
from sklearn.preprocessing import LabelEncoder 
import graphviz 
import matplotlib.pyplot as plt 
from sklearn.metrics import roc_auc_score 
import numpy as np

le = LabelEncoder()

classifier = tree.DecisionTreeClassifier(
    min_impurity_decrease= .01
)

_data  = pd.read_csv('data/training_data.csv')
_data.drop_duplicates(keep="first",inplace=True)
feature_names = _data.iloc[:,:-2].columns 
class_names = list(_data.iloc[:,-2].unique())

X = _data.iloc[:,:-2]
y = _data.iloc[:,-2] 

le.fit(y)
_data.iloc[:,-2] = le.transform(y) 
y = _data.iloc[:,-2]

classifier = classifier.fit(X,y)

n = len(X.iloc[0,:])
inputV = np.array([0 for i in range(n)])
inputV = inputV.reshape(1,len(inputV))

print(feature_names)
feature_names = list(feature_names)

inputV = pd.DataFrame(inputV, columns=feature_names )
index = []
while True : 
    print("Enter symptoms : ",end = " ")
    symptoms = input().split()
    print(symptoms)
    for symptom in symptoms : 
        if symptom in feature_names : 
            inputV.loc[0,symptom] = 1 
    print("Do you want to add more symptoms :(Y/n) ", end=" ") 
    decision = input() 
    if ( not (decision == 'y' or decision=='Y')  ):
        prediction = classifier.predict_proba(inputV).reshape(-1)
        maximum = max(prediction)
        for  i in range(len(prediction)) : 
            if prediction[i] == maximum : 
                index.append(i)
        prediction = le.inverse_transform(index)
        print("\nYou might have {} disease. Kindly consult with your doctor.".format(prediction))
        break 


    
    


# dot_data = tree.export_graphviz(classifier, feature_names = feature_names, class_names = class_names)
# graph = graphviz.Source(dot_data)
# graph.render("_data")


# test_data = pd.read_csv('data/test_data.csv')
# X_test = test_data.iloc[:,:-1]
# y_test = test_data.iloc[:,-1]
# y_test = le.transform(y_test)
# y_pred = classifier.predict_proba(X_test)
# roc_auc = roc_auc_score(y_true=y_test,y_score=y_pred,multi_class='ovr')
# print(roc_auc)



'''
criterion="mse",
splitter="best",
max_depth=None,
min_samples_split=2,
min_samples_leaf=1,
min_weight_fraction_leaf=0.,
max_features=None,
random_state=None,
max_leaf_nodes=None,
min_impurity_decrease=0.,
min_impurity_split=None,
ccp_alpha=0.0)

'''