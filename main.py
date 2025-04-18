from scripts.data_loading import load_sales_data
from scripts.data_cleaning import clean_sales_data
from scripts.analysis import SalesAnalyzer
from scripts.visualization import SalesVisualizer

def main():
    # Load data
    file_path = 'data/retail_sales_dataset.csv'
    sales_df = load_sales_data(file_path)
    
    if sales_df is not None:
        # Clean data
        sales_df = clean_sales_data(sales_df)
        
        # Initialize analyzer and visualizer
        analyzer = SalesAnalyzer(sales_df)
        visualizer = SalesVisualizer(sales_df)
        
        # Perform analysis
        monthly_sales = analyzer.monthly_sales()
        category_sales = analyzer.sales_by_category()
        top_customers = analyzer.top_customers()
        
        print("\nMonthly Sales:")
        print(monthly_sales)
        
        print("\nSales by Category:")
        print(category_sales)
        
        print("\nTop Customers:")
        print(top_customers)
        
        # Generate visualizations
        visualizer.plot_monthly_sales()
        visualizer.plot_sales_by_category()
        visualizer.plot_age_distribution()
        visualizer.plot_sales_heatmap()

if __name__ == "__main__":
    main()