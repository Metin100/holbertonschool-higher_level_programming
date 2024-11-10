from flask import Flask, render_template, request
import os
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)
    
def read_csv(file_path):
    products = []
    with open(file_path) as file:
        datas = csv.DictReader(file)
        for data in datas:
            data['id'] = int(data['id'])
            data['price'] = float(data['price'])
            products.append(data)
    return products

def read_sql(file_path):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'category' : row[2],
            'price' : row[3]
        }
        products.append(product)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    file_path = ''

    if source == 'json':
        file_path = 'products.json'
    elif source == 'csv':
        file_path = 'products.csv'
    elif source == 'sql':
        file_path = 'products.db'
    else:
        return render_template('product_display.html', error = 'Wrong source')
    
    if not os.path.exists(file_path):
        return render_template('product_display.html', error = 'File not exists')
    
    if source == 'json':
        products = read_json(file_path)
    elif source == 'csv':
        products = read_csv(file_path)
    else:
        products = read_sql(file_path)

    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error='Product not found')
    return render_template('product_display.html', products=products)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)