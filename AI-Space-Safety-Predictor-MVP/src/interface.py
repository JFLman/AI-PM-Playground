from predictor import SafetyPredictor

def main():
    # Initialize predictor
    predictor = SafetyPredictor("../data/telemetry_data.csv")

    # Simulate real-time telemetry input
    print("Enter telemetry data (or type 'exit' to quit):")
    while True:
        user_input = input("Engine Temp, Pressure, Stress Level (e.g., 85,120,0.5): ")
        if user_input.lower() == 'exit':
            break

        try:
            telemetry_data = [float(x) for x in user_input.split(',')]
            if len(telemetry_data) != 3:
                raise ValueError("Please enter 3 values.")

            # Get prediction
            prediction, probability, recommendation = predictor.predict(telemetry_data)
            status = "Failure Predicted" if prediction == 1 else "No Failure Predicted"

            # Display results
            print(f"\nPrediction: {status}")
            print(f"Failure Probability: {probability:.2%}")
            print(f"Recommendation: {recommendation}\n")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()