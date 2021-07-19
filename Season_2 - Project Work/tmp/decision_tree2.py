import pandas as pd 
from sklearn import tree
from sklearn.base import ClassifierMixin 
import numpy as np
from sklearn.preprocessing import LabelEncoder 

le = LabelEncoder()

# load data 
data = pd.read_csv("data/training_data.csv")
data.drop('Unnamed: 133',inplace=True,axis=1)

# initialize classification tree object 
classification_tree = tree.DecisionTreeClassifier()


le.fit(data.iloc[:,-1])
print(data.columns)
data.iloc[:,-1] = le.transform(data.iloc[:,-1])
print(le.classes_)
features  = [ list(x) for x in np.array(data.iloc[:,:-1]) ]
target = list(data.iloc[:,-1])

# train decision tree
classification_tree = classification_tree.fit(features,target)

import graphviz 
dot_data = tree.export_graphviz(classification_tree, out_file=None, 
                     feature_names=list(data.columns[:-1]),  
                     class_names=list(data.columns[-1]),  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)


