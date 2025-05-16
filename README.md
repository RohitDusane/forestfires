# Flask App for Predicting Fire Weather Index (FWI)

This Flask web application predicts the **Fire Weather Index (FWI)** using data from **Alegerinc forest fires** and a **Ridge Regression** model.

## Overview

The app takes input features related to forest fires and predicts the Fire Weather Index (FWI), which is a measure of fire danger based on weather conditions. The model is trained using **Ridge Regression**, a type of regularized linear regression that helps to handle collinearity in the dataset.

## Requirements

Before running the app, you need to install the required dependencies:

1. Python 3.6+
2. Flask
3. scikit-learn
4. pandas
5. numpy

You can install the required libraries with:

```bash
pip install -r requirements.txt
```

## Setting Up the Application
1. Clone the repository:
```bash
git clone https://github.com/your-username/fire-weather-index-prediction.git
cd fire-weather-index-prediction
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask application:
```bash
python app.py
```


## Model Description
The Ridge Regression model is used to predict the Fire Weather Index (FWI) based on various meteorological features, including:
* Temperature
* Humidity
* Wind Speed
* Rainfall
* Other relevant features related to forest fire risk
The model was trained using historical data from Alegerinc forest fires and uses regularization to avoid overfitting and improve the generalization of predictions.

## Acknowledgements
* Data used from Alegerinc Forest Fires dataset.

* The Ridge Regression algorithm was implemented using scikit-learn.
