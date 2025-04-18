import matplotlib.pyplot as plt
import seaborn as sns

class SalesVisualizer:
    def __init__(self, df):
        self.df = df
    
    def plot_monthly_sales(self):
        """Plot monthly sales trend"""
        monthly = self.df.resample('ME', on='Date')['Total Amount'].sum()
        plt.figure(figsize=(12, 6))
        monthly.plot(kind='line', marker='o')
        plt.title('Monthly Sales Trend')
        plt.ylabel('Total Sales')
        plt.grid(True)
        plt.show()
    
    def plot_sales_by_category(self):
        """Plot sales by product category"""
        sales_by_cat = self.df.groupby('Product Category')['Total Amount'].sum()
        plt.figure(figsize=(10, 6))
        sales_by_cat.plot(kind='bar')
        plt.title('Sales by Product Category')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.show()
    
    def plot_age_distribution(self):
        """Plot customer age distribution"""
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='Age', bins=20, kde=True)
        plt.title('Customer Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.show()
    
    def plot_sales_heatmap(self):
        """Plot heatmap of sales by category and gender"""
        pivot = self.df.pivot_table(index='Product Category', 
                                   columns='Gender', 
                                   values='Total Amount', 
                                   aggfunc='sum')
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot, annot=True, fmt=".0f", cmap='YlGnBu')
        plt.title('Sales by Category and Gender')
        plt.show()