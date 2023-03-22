import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
import pickle
import json


def model(*args):

    df = pd.read_csv("/home/user/deneme/machine_learning_project/model/customer_shopping_data.csv")
    df.drop(['invoice_no', 'customer_id', 'gender', 'age','quantity',
       'payment_method', 'invoice_date'],axis = 1, inplace=True)
    dummies_category = pd.get_dummies(df.category)
    dummies_shopping_mall = pd.get_dummies(df.shopping_mall)
    df3 = pd.concat([df.drop(["category","shopping_mall"], axis = 1),dummies_category,dummies_shopping_mall],axis='columns')
    X = df3.drop(["price"],axis = 'columns')
    y = df3.price
    X.columns = [each.lower() for each in X.columns]
    x = X.values
    Y = y.values
    X_train, X_test, y_train, y_test = train_test_split(x,Y,test_size=0.3,random_state=10)
    lr_clf = LinearRegression()
    lr_clf.fit(X_train,y_train)
    lr_clf.score(X_test,y_test)
    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
    cross_val_score(LinearRegression(), X, y, cv=cv)

    try:
        loc_index = list(X.columns).index(args[0].lower())
        loc_index1 = list(X.columns).index(args[1].lower())
    except:
        loc_index = -1
        loc_index1 =  -1

    a = np.zeros(len(X.columns))
    if loc_index >= 0:
        a[loc_index] = 1
    if loc_index1 >= 0:
        a[loc_index1] = 1

    return lr_clf.predict([a])[0]
    
    """
    with open("model.pickle","wb") as f:
        pickle.dump(lr_clf,f)
    columns = {
            'data_columns' : [col.lower() for col in X.columns]
        }
    with open("columns.json","w") as f:
        f.write(json.dumps(columns))
        """



if __name__ == "__main__":
    model()
    
