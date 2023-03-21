from flask import Flask, request, jsonify ,render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_category_name',methods = ["GET"])
def get_category_names():
    response = jsonify({
        'category' : util.get_category_name()   
    })
    response.headers.add("Acces-control-Allow-Origin","*")
    
    return response

@app.route('/get_shopping_mall_name')
def get_shopping_mall_names():
    response = jsonify({
        'shopping_mall' : util.get_shopping_mall_name()
    })
    response.headers.add("Acces-control-Allow-Origin","*")
    
    return response

@app.route('/get_predict',methods = ["POST"])
def predict_price():
    category = request.form["category"]
    shopping_mall = request.form["shopping_mall"]

    response = jsonify({
        "estimated_price" : util.get_estimated_price(category,shopping_mall)
    })

    return response

if __name__ == "__main__" :
    print("Starting Python Flask Server For Home Price Prediction..")
    util.load_saved_artifacts()
    app.run(debug=True)