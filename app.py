import streamlit as st
import pandas as pd
from scripts.data_loading import load_sales_data
from scripts.data_cleaning import clean_sales_data
from scripts.analysis import SalesAnalyzer
from scripts.visualization import SalesVisualizer

st.set_page_config(page_title="Sales Data Dashboard", layout="wide")
st.title("📊 Sales Data Analysis Dashboard")

# Sidebar navigation
page = st.sidebar.radio("Select a section", ["📥 Upload & Preview", "📈 Analysis", "📊 Visualizations"])

# Load and clean data
@st.cache_data

def load_and_clean(file_path):
    df = load_sales_data(file_path)
    return clean_sales_data(df)

file_path = "data/retail_sales_dataset.csv"
sales_df = load_and_clean(file_path)

if sales_df is not None:
    analyzer = SalesAnalyzer(sales_df)
    visualizer = SalesVisualizer(sales_df)

    if page == "📥 Upload & Preview":
        st.subheader("🔍 Data Preview")
        st.dataframe(sales_df.head(50), use_container_width=True)

        st.subheader("📌 Summary Statistics")
        st.dataframe(sales_df.describe(), use_container_width=True)

        st.markdown(f"**🧾 Total Records:** {len(sales_df)}")

    elif page == "📈 Analysis":
        st.subheader("🗓 Monthly Sales")
        monthly_sales = analyzer.monthly_sales()
        st.line_chart(monthly_sales, use_container_width=True)

        st.subheader("🛍 Sales by Category")
        category_sales = analyzer.sales_by_category()
        st.bar_chart(category_sales, use_container_width=True)

        st.subheader("👑 Top Customers")
        st.dataframe(analyzer.top_customers(), use_container_width=True)

    elif page == "📊 Visualizations":
        st.subheader("🗓 Monthly Sales Trend")
        visualizer.plot_monthly_sales()

        st.subheader("📦 Sales by Product Category")
        visualizer.plot_sales_by_category()

        st.subheader("👥 Customer Age Distribution")
        visualizer.plot_age_distribution()

        st.subheader("🔥 Heatmap: Category vs Gender")
        visualizer.plot_sales_heatmap()
else:
    st.error("❌ Failed to load data. Please check the file path or file format.")
