import pickle
import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the wine model
MODEL_PATH = "model/wine_model.pkl"
if not os.path.exists(MODEL_PATH):
    raise Exception(
        "Model file not found at '{}'. Make sure to train the model by running 'train.py'.".format(MODEL_PATH)
    )

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Home route to display the form
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route to handle form submissions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract 13 wine features from the form and convert to float
        features = [float(x) for x in request.form.values()]
        
        if len(features) != 13:
            return render_template("index.html", prediction_text="Error: Please enter all 13 features.")

        # Make a prediction using the model
        prediction = model.predict([features])[0]

        # Display the prediction result
        return render_template(
            "index.html", prediction_text=f"Predicted Wine Class: {prediction}"
        )

    except ValueError:
        return render_template("index.html", prediction_text="Invalid input: Please enter valid numbers.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

