from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from boston_price_prediction.boston_price_prediction import BostonPricePrediction

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homePage():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        features = request.form
        predicted_price = BostonPricePrediction().predict(features)
        predicted_price = round(predicted_price[0], 2)
        return render_template('index.html', response = {'features': features, 'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)


