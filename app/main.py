from flask import Flask, render_template, request
import utils
import os
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', categories=utils.get_categories())


@app.route('/products')
def category_product_controller():
    id = request.args.get('category_id', default = 0, type = int)
    if id==0:
        return render_template('products.html', products=utils.get_products())
    return render_template('products.html', products=utils.get_category(id))


@app.route('/products')
def products_controller():
    return render_template('products.html', products=utils.get_products())


@app.route('/products/<offset>')
def product_controller(offset=1):
    return render_template('product.html', product=utils.get_product(offset))


if __name__ == '__main__':
    app.run(debug=True)
