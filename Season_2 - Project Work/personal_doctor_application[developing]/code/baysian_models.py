'''
Variants of navie bayes -- only differ in condition of independence between features 

Gaussian Naive Bayes -- Assume gaussian distribution of features in space 
Augmented Naive Bayes -- It took into consideration of dependence between nodes 
Multinomial Naive Bayes -- 
Complement Naive Bayes 
Categorical Naive Bayes 
Bernoulli Naive Bayes 
Categorical Naive Bayes 
'''

import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB 

train_data = pd.read_csv('train.csv')
print(train_data.columns)
y = train_data[['prognosis']]
train_data.drop('prognosis',axis=1,inplace=True)
train_data.drop('Unnamed: 133',axis=1,inplace=True)
X = train_data 

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,shuffle=False)

y_pred = GaussianNB().fit(X_train,y_train).predict(X_test)
print(y_pred.shape)
print(y_pred[0:10])
print(y_test[0:10])
# print(f"No of labels out of {X_test.shape[0]} incorrectly classified {(y_pred != y_test).sum()}")