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
from sklearn.preprocessing import LabelEncoder 

le  = LabelEncoder()

train_data = pd.read_csv('train.csv')
train_data.drop_duplicates(inplace=True)
test_data = pd.read_csv('test.csv')
train_data.drop('Unnamed: 133',inplace=True,axis=1)
y_train = train_data.loc[:,['prognosis']]
y_test = test_data.loc[:,['prognosis']]
le.fit(y_train)

y_train = le.transform(y_train)
y_test = le.transform(y_test)

train_data.drop('prognosis',axis=1,inplace=True)
test_data.drop('prognosis',axis=1,inplace=True)
X_train = train_data 
X_test = test_data

cnt_gnb, cnt_mnb , cnt_cnb, cnt_bnb, cnt_cat_nb = 0,0,0,0,0

n = 100

for i in range(n) : 
    print(i+1)
    y_pred_gnb = GaussianNB().fit(X_train,y_train).predict(X_test)
    y_pred_mnb = MultinomialNB().fit(X_train,y_train).predict(X_test)
    y_pred_cnb = ComplementNB().fit(X_train,y_train).predict(X_test)
    y_pred_bnb = BernoulliNB().fit(X_train,y_train).predict(X_test)
    y_pred_cat_nb = CategoricalNB().fit(X_train,y_train).predict(X_test)

    cnt_gnb += (y_pred_gnb != y_test).sum() 
    cnt_mnb += (y_pred_mnb != y_test).sum()
    cnt_cnb += (y_pred_cnb != y_test).sum()
    cnt_bnb += (y_pred_bnb != y_test).sum()
    cnt_cat_nb += (y_pred_cat_nb != y_test).sum() 


print(f"No of labels out of {X_test.shape[0]} in 'Gaussian' on average incorrectly classified {cnt_gnb//n}")
print(f"No of labels out of {X_test.shape[0]} in 'Multinomial' on  average incorrectly classified {cnt_mnb//n}")
print(f"No of labels out of {X_test.shape[0]} in 'Complement' on average incorrectly classified {cnt_cnb//n}")
print(f"No of labels out of {X_test.shape[0]} in 'Bernoulli' on average incorrectly classified {cnt_bnb//n}")
print(f"No of labels out of {X_test.shape[0]} in 'Categorical' on average incorrectly classified {cnt_cat_nb//n}")


'''
Conclusion : For given dataset it seems like gaussian model is giving promising results.
'''