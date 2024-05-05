from flask import Flask,render_template
from cupcakes import get_cupcakes

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', cupcakes=get_cupcakes("cupcakes.csv"))

@app.route('/singlecupcake')
def single_cupcake():
    return render_template('cupcake.html')

@app.route('/allcupcake')
def all_cupcake():
    return render_template('all-cupcake.html')

@app.route('/order')
def acive_order():
    return render_template('order.html')


if __name__=="__main__":
    app.env="development"
    app.run(debug=True, port=8000,host='localhost')

