from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('diabetes_logistic_regression_model.pkl')

# Create a Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Collect data from the form
    try:
        input_data = [float(x) for x in request.form.values()]
        input_data_as_numpy = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy.reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data_reshaped)

        # Result message
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template('index.html', prediction_text='Prediction: {}'.format(result))
    except ValueError:
        return render_template('index.html', prediction_text='Error: Please enter valid numeric values.')

if __name__ == "__main__":
    app.run(debug=True)
