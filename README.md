E-Commerce Sales & Delivery Insights Analyzer

Description

The E-Commerce Sales & Delivery Insights Analyzer is a data analysis project built using Python that processes and analyzes an e-commerce dataset to uncover key business insights.

The project focuses on:

Identifying top-selling products Determining top-performing sellers by revenue Analyzing delivery times Tracking monthly revenue trends

It also generates interactive visualizations using Plotly, making it easy to explore patterns and performance metrics.

Features

Merge and clean multiple datasets
Calculate delivery time statistics (average, min, max, range)
Generate histogram for delivery time distribution
Identify top 10 most sold products
Identify top 10 sellers by total revenue
Visualize monthly revenue trends
Export interactive charts as HTML files
Technologies Used

Python
Pandas (data manipulation)
Plotly (data visualization)
Installation Prerequisites Python 3.x installed pip package manager Install Dependencies pip install pandas plotly

▶ Usage Place the dataset files in your project directory: olist_orders_dataset.csv olist_order_items_dataset.csv Run the script: python main.py Output generated: Console statistics (delivery time, revenue, etc.) Interactive HTML files: delivery_time_histogram.html top_10_products_bar_chart.html top_10_sellers_revenue_bar_chart.html olist_monthly_revenue_trend.html Open the HTML files in your browser to explore the visualizations.

Example Insights Average delivery time across all orders Top 10 products based on sales volume Top 10 sellers based on revenue Monthly revenue growth trends

Configuration

You can customize the project by modifying:

File paths pd.read_csv('your_file.csv') Top N results head(10) # Change to head(5), head(20), etc. Date formatting dt.strftime('%Y-%m') Revenue calculation logic price + freight_value

Project Structure ecommerce-analysis/ │ ├── main.py # Main analysis script ├── olist_orders_dataset.csv # Orders dataset ├── olist_order_items_dataset.csv # Order items dataset ├── delivery_time_histogram.html # Output visualization ├── top_10_products_bar_chart.html # Output visualization ├── top_10_sellers_revenue_bar_chart.html# Output visualization ├── olist_monthly_revenue_trend.html # Output visualization └── README.md # Project documentation

Troubleshooting

File not found error Ensure CSV files are in the correct directory Check file names for typos
Encoding issues Try: pd.read_csv('file.csv', encoding='latin1')
Plot not opening Ensure browser is installed Open HTML files manually if auto_open=True fails
Missing data (NaN values) The script drops missing delivery times: dropna(subset=['delivery_time_days'])
Contributing

Contributions are welcome.

Fork the repository Create a feature branch: git checkout -b feature-name Commit your changes: git commit -m "Add feature" Push to your branch: git push origin feature-name Open a Pull Request

License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.
