import pandas as pd

def clean_sales_data(df):
    """
    Clean the sales data by handling missing values, converting data types, etc.
    Ensures datetime column is Arrow-safe for Streamlit display.
    """

    # Convert to datetime, remove failed conversions
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # 🔥 Absolute fix: Remove nanoseconds completely and enforce datetime64[ns]
    df['Date'] = df['Date'].apply(lambda x: pd.to_datetime(x.strftime('%Y-%m-%d %H:%M:%S')))

    # Handle any remaining missing values
    if df.isnull().sum().sum() > 0:
        print("Warning: Other missing values found. Dropping them.")
        df = df.dropna()

    return df
