from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load your trained model
model = load_model('/content/rossmann_sales_lstm_model.h5')

# Define the features used during training
FEATURES = ['Year', 'DaysToHoliday', 'Customers', 'Month']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_features = [data[feature] for feature in FEATURES]
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)
    return jsonify({"prediction": float(prediction[0][0])})

# Run Flask app
app.run(port=5000)
