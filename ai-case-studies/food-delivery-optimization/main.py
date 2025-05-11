import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

# Analyze the dataset
def analyze_data(df):
    """Perform basic analysis on the dataset."""
    print("Dataset Overview:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())

# Visualize data
def visualize_data(df):
    """Generate visualizations for key insights."""
    # Distribution of order amounts
    plt.figure(figsize=(10, 6))
    sns.histplot(df['cost_of_the_order'], kde=True, bins=30, color='blue')
    plt.title('Distribution of Order Amounts')
    plt.xlabel('Order Amount')
    plt.ylabel('Frequency')
    plt.show()

    # Average delivery time by day of the week
    plt.figure(figsize=(10, 6))
    sns.barplot(x='day_of_week', y='delivery_time', data=df, ci=None, palette='viridis')
    plt.title('Average Delivery Time by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Delivery Time (minutes)')
    plt.show()

# Main function
def main():
    """Main function to execute the analysis."""
    # File path to the dataset
    file_path = 'data/food_delivery_data.csv'  # Update with the actual file path

    # Load data
    df = load_data(file_path)

    # Analyze data
    analyze_data(df)

    # Visualize data
    visualize_data(df)

if __name__ == "__main__":
    main()
