from flask import Flask, request, render_template
from src.predictor import SafetyPredictor

app = Flask(__name__)

# Initialize the predictor
predictor = SafetyPredictor("data/telemetry_data.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            engine_temp = float(request.form["engine_temp"])
            pressure = float(request.form["pressure"])
            stress_level = float(request.form["stress_level"])

            prediction, probability, recommendation = predictor.predict_failure(
                engine_temp, pressure, stress_level
            )
            result = {
                "prediction": "Failure Predicted" if prediction else "No Failure Predicted",
                "probability": f"{probability * 100:.2f}%",
                "recommendation": recommendation
            }
            return render_template("index.html", result=result)
        except ValueError:
            error = "Please enter valid numerical values."
            return render_template("index.html", error=error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)