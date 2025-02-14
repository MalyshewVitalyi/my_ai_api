from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Загрузка модели
model = joblib.load("ai_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([
        data['Close'], data['RSI'], data['ATR']
    ]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({'signal': 'Buy' if prediction == 1 else 'Sell'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)