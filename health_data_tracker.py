import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def load_health_data(file_path):
    """
    Load health data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path, parse_dates=['Date'])
        return data
    except Exception as e:
        print(f"Error loading health data: {str(e)}")
        return None

def track_body_weight(data, new_entry):
    """
    Track and visualize body weight over time.
    """
    if data is None:
        return

    # Add new entry to the dataset
    data = data.append(new_entry, ignore_index=True)

    # Visualize body weight over time
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Weight'], marker='o', linestyle='-', color='b')
    plt.title('Body Weight Over Time')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.grid(True)
    plt.show()

    # Save the updated dataset
    data.to_csv('health_data.csv', index=False)

if __name__ == "__main__":
    # Sample health data (replace with your own dataset)
    file_path = 'health_data.csv'
    
    # Load existing health data or create a new dataset
    health_data = load_health_data(file_path) if file_path else pd.DataFrame(columns=['Date', 'Weight'])

    # Get a new entry from the user (for simplicity, enter today's date and weight)
    new_date = input("Enter the date (YYYY-MM-DD): ").strip()
    new_weight = float(input("Enter your weight (kg): ").strip())

    new_entry = {'Date': datetime.strptime(new_date, '%Y-%m-%d'), 'Weight': new_weight}

    # Track and visualize body weight
    track_body_weight(health_data, new_entry)
