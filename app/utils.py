import os
import json

from flask.sessions import NullSession
from main import app



def get_categories():
    with open(os.path.join(app.root_path, 'data/categories.json'), encoding="utf-8") as f:
        return json.load(f)


def get_category(id):
    data=[]
    with open(os.path.join(app.root_path, 'data/products.json'), encoding="utf-8") as f:
        for i in json.load(f):
            if i['category_id'] == id:
                data.append(i)
    return data
 



def get_products():
    with open(os.path.join(app.root_path, 'data/products.json'), encoding="utf-8") as f:
        return json.load(f)




def get_product(id):
    with open(os.path.join(app.root_path, 'data/products.json'), encoding="utf-8") as f:
        for i in json.load(f):
            if i['id'] == id:
                return i
        return i

