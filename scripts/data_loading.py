import pandas as pd

def load_sales_data(file_path):
    """
    Load sales data from a CSV file
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None