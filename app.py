from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("models/energy_model.pkl")

@app.route('/')
def home():
    return "AI Energy Forecasting API Running Successfully!"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    features = np.array([[
        data['hour'],
        data['dayofweek'],
        data['month'],
        data['year'],
        data['lag1'],
        data['lag24'],
        data['lag168']
    ]])

    prediction = model.predict(features)

    return jsonify({
        "Predicted Energy Usage": float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)