from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
# Load mô hình nhận diện bất thường
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        # Chạy dự đoán
        prediction = model.predict(df)
        status = "Anomaly" if prediction[0] == 1 else "Nominal"
        return jsonify({"status": status})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)