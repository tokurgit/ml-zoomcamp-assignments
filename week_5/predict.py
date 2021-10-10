from flask import jsonify, request
from flask import Flask
import pickle


with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)
with open('model1.bin', 'rb') as model_file:
    model = pickle.load(model_file)


customer = {
    "contract": "two_year",
    "tenure": 12,
    "monthlycharges": 19.7
}

app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        "churn_probability": round(float(y_pred), 3)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9697)
