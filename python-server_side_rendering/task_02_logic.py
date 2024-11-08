from flask import Flask, render_template
from json import load

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = load(file)
        items = data.get('items') or []
    return render_template('templates/items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)