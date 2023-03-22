import json
import pickle
import numpy as np

__category = None
__shopping_mall = None
__data_columns = None
__model = None

def load_saved_artifacts():

    print("loadin saved artifacts....start")
    
    global __data_columns
    global __category
    global __shopping_mall
    global __model

    with open("/home/user/deneme/machine_learning_project/server/artifacts/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __category = __data_columns[0:8]
        __shopping_mall = __data_columns[8:]

    with open("/home/user/deneme/machine_learning_project/server/artifacts/model.pickle" , "rb") as f:
        __model = pickle.load(f)
    
    print("loadin saved artifacts....done")

    return __category, __shopping_mall, __model

def get_category_name():
    
    return __category

def get_shopping_mall_name():

    return __shopping_mall

def get_estimated_price(category,shopping_mall):
    try:
        loc_index = __data_columns.index(category.lower())
        loc_index1 = __data_columns.index(shopping_mall.lower())
    except:
        loc_index = -1
        loc_index1 =  -1

    x = np.zeros(len(__data_columns))
    if loc_index >= 0:
        x[loc_index] = 1
    if loc_index1 >= 0:
        x[loc_index1] = 1
    return __model.predict([x])[0]

if __name__ == "__main__":
    load_saved_artifacts()
    print(__data_columns)
    print(get_estimated_price("clothing","kanyon"))
    
    

    
    