from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('gdp_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        investment = float(request.form['investment'])
        consumption = float(request.form['consumption'])
        exports = float(request.form['exports'])

        features = np.array([[investment, consumption, exports]])
        prediction = model.predict(features)[0]

        return jsonify({'predicted_gdp': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)