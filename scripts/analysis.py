import pandas as pd

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df
    
    def monthly_sales(self):
        """Calculate monthly sales"""
        monthly = self.df.resample('M', on='Date')['Total Amount'].sum()
        return monthly
    
    def sales_by_category(self):
        """Calculate sales by product category"""
        return self.df.groupby('Product Category')['Total Amount'].sum()
    
    def sales_by_gender(self):
        """Calculate sales by gender"""
        return self.df.groupby('Gender')['Total Amount'].sum()
    
    def top_customers(self, n=10):
        """Identify top customers by total spending"""
        return (self.df.groupby('Customer ID')
                .agg({'Total Amount': 'sum', 'Gender': 'first', 'Age': 'first'})
                .sort_values('Total Amount', ascending=False)
                .head(n))
    
    def customer_age_analysis(self):
        """Analyze sales by customer age groups"""
        bins = [0, 20, 30, 40, 50, 60, 100]
        labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60+']
        self.df['Age Group'] = pd.cut(self.df['Age'], bins=bins, labels=labels)
        return self.df.groupby('Age Group')['Total Amount'].sum()