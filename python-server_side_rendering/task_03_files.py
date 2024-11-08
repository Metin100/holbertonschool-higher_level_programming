from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json(file_path):
    with open(file_path):
        return json.load(file_path)
    
def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
    for row in reader:
        row['id'] = int(row['id'])
        row['price'] = int(row['price'])
        products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    file_path = ''

    if source == 'json':
        file_path = 'products.json'
    if source == 'csv':
        file_path == 'products.csv'
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")


    if source == 'json':
        products = read_json(file_path)

    if source == 'csv':
        products = read_csv(file_path)

    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error = 'Product not found')
    return render_template('product_display.html', products = products)
if __name__ == '__main__':
    app.run(debug=True, port=5000)