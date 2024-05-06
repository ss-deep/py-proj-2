from flask import Flask,render_template
from cupcakes import get_cupcakes, find_cupcake, add_order

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html' )

@app.route('/singlecupcake')
def single_cupcake():
    return render_template('cupcake.html')

@app.route('/allcupcake/<type>')
def all_cupcake(type):
    # print(type)
    if type=='all':
        cupcakes=get_cupcakes("cupcakes.csv")
    elif type=='cart':
        cupcakes=get_cupcakes("order.csv")
    # print(cupcakes)
    return render_template('all-cupcake.html',cupcakes=cupcakes)

@app.route('/add/<name>')
def add_to_cart(name):
    cupcakes=add_order('order.csv',name)
    # print(cupcakes)
    return render_template('order.html',cupcakes=cupcakes)
    

# @app.route('/order/<name>')
# def acive_order(name):
#     return render_template('order.html',cupcake=find_cupcake('order.csv',name))


if __name__=="__main__":
    app.env="development"
    app.run(debug=True, port=8000,host='localhost')

