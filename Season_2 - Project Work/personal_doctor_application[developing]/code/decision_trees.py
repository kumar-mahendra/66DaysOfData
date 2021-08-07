from sklearn import tree 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np 
le = LabelEncoder()
ohe = OneHotEncoder()
import warnings 
from sklearn.model_selection import cross_val_score as cvs
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier

warnings.filterwarnings('ignore')


# Prepare dataset 
#######################################################

# import data 
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_data.drop_duplicates(inplace=True)
train_data.drop('Unnamed: 133',inplace=True,axis=1)
y_train = train_data.loc[:,['prognosis']]
y_test = test_data.loc[:,['prognosis']]

# print(y_train['prognosis'].unique())
# print(y_test['prognosis'].unique())

# print(len(set(y_train['prognosis'].unique())),len(set(y_test['prognosis'].unique())))
# A, B = set(y_train['prognosis'].unique()), set(y_test['prognosis'].unique())
# print(B.difference(A))

X_train = np.array( train_data.drop('prognosis',axis=1) )
X_test = np.array( test_data.drop('prognosis',axis=1) ) 


le.fit(y_train)

y_train = le.transform(y_train).reshape(-1,1)  # label encoding 
ohe.fit(y_train)
y = ohe.transform(y_train).toarray()  # one-hot encoding 
y_test = le.transform(y_test)



# Model without ensembling 
#############################################################

y_pred = tree.DecisionTreeClassifier().fit(X_train,y).predict(X_test)
y_pred = ohe.inverse_transform((y_pred)).reshape(-1)
print(f"No of labels out of {X_test.shape[0]} in 'Decision Tree Classifier' are incorrectly classified {(y_pred != y_test).sum()}")


# Models with ensembling 
###########################################################

y_pred = BaggingClassifier( tree.DecisionTreeClassifier(), max_samples=0.5).fit(X_train,y_train).predict(X_test)
print(f"No of labels out of {X_test.shape[0]} in 'Bagging Classifier' are incorrectly classified {(y_pred != y_test).sum()}")


y_pred = RandomForestClassifier(n_estimators=10,max_features="sqrt").fit(X_train,y).predict(X_test)
y_pred = ohe.inverse_transform((y_pred)).reshape(-1)
print(f"No of labels out of {X_test.shape[0]} in 'Random Forest Classifier' are incorrectly classified {(y_pred != y_test).sum()}")


y_pred = ExtraTreesClassifier(n_estimators=20).fit(X_train,y).predict(X_test)
y_pred = ohe.inverse_transform((y_pred)).reshape(-1)
print(f"No of labels out of {X_test.shape[0]} in 'Extra Trees Classifier' are incorrectly classified {(y_pred != y_test).sum()}")

y_pred = AdaBoostClassifier(n_estimators=10).fit(X_train,y_train).predict(X_test)
# y_pred = ohe.inverse_transform((y_pred)).reshape(-1)
print(f"No of labels out of {X_test.shape[0]} in 'Extra Trees Classifier' are incorrectly classified {(y_pred != y_test).sum()}")

































































# ### finding incorrect classification 
# for i in range(len(y_test)) : 
#     if (y_test[i] != y_pred[i]) : 
#         true, pred = le.inverse_transform([y_test[i]])[0],le.inverse_transform([y_pred[i]])[0]
#         # true, pred = '_'.join(true.lower().split()), '_'.join(pred.lower().split())
#         print(f"Actual : {true} , Predicted : {pred}")
        
#         # finding symptoms of respective diseases 
#         train = pd.read_csv('train.csv').drop('Unnamed: 133',axis=1)
#         train = train[train['prognosis']==true]
#         # print(train)
#         symptoms = []
        
#         for i in range(len(train)) :
#             for col in train.columns[:-1] : 
#                 tmp = train[i:i+1][col].values
#                 try : 
#                     if tmp[0] == 1 : 
#                         symptoms.append(col)
#                 except : 
#                     continue  
#         symptoms = list(set(symptoms))

#         train = pd.read_csv('train.csv').drop('Unnamed: 133',axis=1)
#         train = train[train['prognosis']==pred]
#         symptoms_pred  = []
#         for i in range(len(train)) :
#             for col in train.columns[:-1] : 
#                 tmp = train[i:i+1][col].values
#                 try : 
#                     if tmp[0] == 1 : 
#                         symptoms_pred.append(col)
#                 except : 
#                     continue  
#         symptoms_pred = list(set(symptoms_pred))
#         print(symptoms)
#         print(symptoms_pred)






    
