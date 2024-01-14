# app.py

from flask import Flask, render_template
from scraping import get_taco_bell_items  
app = Flask(__name__)

@app.route('/')
def home():
    items = get_taco_bell_items()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
