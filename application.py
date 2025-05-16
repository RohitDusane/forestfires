import pickle
from flask import Flask, request, render_template
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Function to interpret the FWI value
def interpret_fwi(fwi_value):
    if fwi_value < 5:
        return "Low risk of fire"
    elif 5 <= fwi_value < 10:
        return "Moderate risk of fire"
    elif 10 <= fwi_value < 20:
        return "High risk of fire"
    else:
        return "Very high risk of fire"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        # Get the form data
        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])
        Region = float(request.form['Region'])

        # Prepare the data for prediction
        input_data = pd.DataFrame([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
                                  columns=['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region'])

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make the prediction using the trained Ridge model
        prediction = ridge_model.predict(input_data_scaled)

        # Interpret the FWI prediction
        fwi_interpretation = interpret_fwi(prediction[0])

        # Debugging: Print the prediction and interpretation
        print("Prediction:", prediction[0])
        print("Interpretation:", fwi_interpretation)

        # Return the result with interpretation
        return render_template('home.html', result=prediction[0], interpretation=fwi_interpretation)
        
    # If it's a GET request, just render the home page with no prediction
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
