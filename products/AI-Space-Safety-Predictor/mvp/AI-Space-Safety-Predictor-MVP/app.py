from flask import Flask, request, render_template
import pandas as pd
import plotly.graph_objects as go
from src.predictor import SafetyPredictor

app = Flask(__name__)
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

            # Generate plot of historical data
            data = pd.read_csv("data/telemetry_data.csv")
            if data['stress_level'].max() > 1.0:
                print("Warning: Stress level exceeds 1.0 in data, capping at 1.0 for plot")
                data['stress_level'] = data['stress_level'].clip(upper=1.0)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data.index, y=data['stress_level'], mode='lines+markers', name='Stress Level'))
            fig.add_trace(go.Scatter(x=data.index, y=data['failure'], mode='markers', name='Failure'))
            fig.update_layout(
                xaxis_title="Data Point Index",
                yaxis_title="Value",
                title="Historical Telemetry Trends"
            )
            plot_html = fig.to_html(full_html=False)

            return render_template("index.html", result=result, plot=plot_html)
        except ValueError:
            error = "Please enter valid numerical values."
            return render_template("index.html", error=error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)