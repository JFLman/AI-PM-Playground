# AI Space Safety Predictor MVP

## Overview
This MVP demonstrates the core functionality of the AI Space Safety Predictor, designed to predict failures in reusable space vehicles using telemetry data and provide preventive recommendations. It supports Blue Origin’s mission of safe, low-cost spaceflight.

## How to Run
1. Clone this repo: `git clone <your-repo-url>`
2. Navigate to the project: `cd AI-Space-Safety-Predictor-MVP`
3. Set up a virtual environment:
   - `python -m venv venv`
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the CLI: `python src/interface.py`
6. Enter telemetry data (e.g., `85,120,0.5`) to get predictions.

## Limitations
- Uses simulated data (expand with real telemetry for production).
- Basic ML model (logistic regression); upgrade to ensemble models.
- CLI interface; future versions will include a dashboard.

## Next Steps
- Integrate real telemetry data from Blue Origin systems.
- Deploy a React-based dashboard for cross-functional teams.
- Enhance model with deep learning (e.g., LSTM for time-series data).