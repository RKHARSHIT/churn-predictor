from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import logging

# -------------------- Logging Configuration --------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
# ---------------------------------------------------------------

app = Flask(__name__)

# -------------------- Model and Scaler Loading --------------------
try:
    model = joblib.load('model/logistic_model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    logger.info("Model and scaler loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load model or scaler: {e}")
    raise
# ------------------------------------------------------------------

# Feature list and numerical columns
features = [
    "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "PaperlessBilling",
    "MonthlyCharges", "TotalCharges", "NumServicesUsed", "IsFiber_and_TechSupport",
    "gender_Male", "MultipleLines_Yes", "InternetService_Fiber optic", "InternetService_No",
    "OnlineSecurity_Yes", "OnlineBackup_Yes", "DeviceProtection_Yes", "TechSupport_Yes",
    "StreamingTV_Yes", "StreamingMovies_Yes", "Contract_One year", "Contract_Two year",
    "PaymentMethod_Credit card (automatic)", "PaymentMethod_Electronic check",
    "PaymentMethod_Mailed check", "tenure_group_Mid-Term", "tenure_group_New",
    "MonthlyChargeGroup_Low", "MonthlyChargeGroup_Medium"
]

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'NumServicesUsed']

# -------------------- Routes --------------------
@app.route("/", methods=["GET", "POST"])
def predict_form():
    prediction = None
    prob_churn = None
    prob_no_churn = None

    if request.method == "POST":
        try:
            logger.info("Received POST request with form data.")
            input_data = [float(request.form[feature]) for feature in features]
            df = pd.DataFrame([input_data], columns=features)

            logger.info(f"Input DataFrame:\n{df}")

            df[num_cols] = scaler.transform(df[num_cols])

            pred = model.predict(df)[0]
            probabilities = model.predict_proba(df)[0]

            prediction = "Churn" if pred == 1 else "No Churn"
            prob_churn = round(probabilities[1], 2)
            prob_no_churn = round(probabilities[0], 2)

            logger.info(f"Prediction: {prediction} | Churn: {prob_churn} | No Churn: {prob_no_churn}")

        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            prediction = "Error processing input"
            prob_churn = prob_no_churn = "N/A"

    return render_template('form.html',
                           features=features,
                           prediction=prediction,
                           prob_churn=prob_churn,
                           prob_no_churn=prob_no_churn
                           )
# -------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
