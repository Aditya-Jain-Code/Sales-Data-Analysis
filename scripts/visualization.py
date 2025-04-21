import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

class SalesVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_monthly_sales(self):
        monthly = self.df.resample('ME', on='Date')['Total Amount'].sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly.plot(kind='line', marker='o', ax=ax)
        ax.set_title('Monthly Sales Trend')
        ax.set_ylabel('Total Sales')
        ax.grid(True)
        st.pyplot(fig)  # Streamlit rendering

    def plot_sales_by_category(self):
        sales_by_cat = self.df.groupby('Product Category')['Total Amount'].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        sales_by_cat.plot(kind='bar', ax=ax)
        ax.set_title('Sales by Product Category')
        ax.set_ylabel('Total Sales')
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    def plot_age_distribution(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=self.df, x='Age', bins=20, kde=True, ax=ax)
        ax.set_title('Customer Age Distribution')
        ax.set_xlabel('Age')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    def plot_sales_heatmap(self):
        pivot = self.df.pivot_table(index='Product Category', 
                                    columns='Gender', 
                                    values='Total Amount', 
                                    aggfunc='sum')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(pivot, annot=True, fmt=".0f", cmap='YlGnBu', ax=ax)
        ax.set_title('Sales by Category and Gender')
        st.pyplot(fig)
