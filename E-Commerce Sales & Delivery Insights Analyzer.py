import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Step 1: Loading the datasets
orders_df = pd.read_csv('olist_orders_dataset.csv', encoding="utf-8")
order_items_df = pd.read_csv('olist_order_items_dataset.csv', encoding="utf-8")


print("\nMerging datasets on 'order_id'.")
combined_orders_dataset = pd.merge(orders_df, order_items_df, on='order_id', how='inner')
print("\nDatasets merged successfully.")
print("Combined dataset shape:", combined_orders_dataset.shape)

# Cleaning Dataset (checking for null values)
print(combined_orders_dataset)

print(orders_df.head()) # Displaying head to verify merge

print("Summary of the data")
print(combined_orders_dataset.info())



print("\nConverting timestamp columns to datetime.")
combined_orders_dataset['order_purchase_timestamp'] = pd.to_datetime(combined_orders_dataset['order_purchase_timestamp'])
combined_orders_dataset['order_delivered_customer_date'] = pd.to_datetime(combined_orders_dataset['order_delivered_customer_date'])
print("Timestamp columns converted.")
print(combined_orders_dataset['order_purchase_timestamp'])
print( combined_orders_dataset['order_delivered_customer_date'])


# Calculating the difference and converting to days
# calculating for 'each order' where delivery date is available.
print("\nCalculating delivery time in days.")
combined_orders_dataset['delivery_time_days'] = (combined_orders_dataset['order_delivered_customer_date'] - combined_orders_dataset['order_purchase_timestamp']).dt.days
print(combined_orders_dataset['delivery_time_days'])


# Removing orders where delivery time could not be calculated for plotting
delivery_times = combined_orders_dataset.dropna(subset=['delivery_time_days'])['delivery_time_days']
print(f"\nNumber of orders with valid delivery times for plotting: {len(delivery_times)}")

print("Creating delivery time histogram using Plotly.")
data = [go.Histogram(x=delivery_times)]

# Defining layout for the plot
layout = go.Layout(
    title="Distribution of Order Delivery Times (in days)",
    xaxis={'title': 'Delivery Time (Days)'}, # Add an x-axis label
    yaxis={'title': 'Frequency'} # Add a y-axis label
)

# Creating a Figure object combining data and layout
fig = go.Figure(data=data, layout=layout)

# Generating an interactive HTML plot file
pyo.plot(fig, filename='delivery_time_histogram.html')


# Calculating the mean of the delivery_time_days column
average_delivery_time = combined_orders_dataset['delivery_time_days'].mean() # .mean() is an aggregation function
print("Average delivery time: " + " " + str(average_delivery_time))


# Calculating the minimum and maximum values
min_delivery_time = combined_orders_dataset['delivery_time_days'].min()
print("Minimum delivery time:" + " " + str(min_delivery_time))
max_delivery_time = combined_orders_dataset['delivery_time_days'].max()
print("Maximum delivery time: " + " " + str(max_delivery_time))
delivery_time_range = max_delivery_time - min_delivery_time
print("Delivery time range:" + " " + str(delivery_time_range))

print("\n--- Delivery Time Statistics ---")
print(f"The average delivery time is: {average_delivery_time:.2f} days") # Formatting to 2 decimal places
print(f"The minimum delivery time is: {min_delivery_time} days")
print(f"The maximum delivery time is: {max_delivery_time} days")
print(f"The range of delivery times is: {delivery_time_range} days")
print("--------------------------------")






# Step 1: Identifying the top 10 most sold products based on the number of items sold.
# Group by 'product_id' and count the number of entries for each product
print("Calculating product sales counts.")
product_sales = combined_orders_dataset.groupby('product_id').size()

# Sorting the results in ascending order and get the top 10
top_10_products = product_sales.sort_values(ascending=False).head(10)
print("\nTop 10 Most Sold Products (by item count):")
print(top_10_products)



# Step 2: Creating a bar chart to display these top-selling products.

product_ids = top_10_products.index.tolist()
sales_counts = top_10_products.values.tolist()

print("\nCreating bar chart for top-selling products using Plotly.")
data = [go.Bar(
    x=product_ids,
    y=sales_counts,
)]

layout = go.Layout(
    title='Top 10 Most Sold Products',
    xaxis={'title': 'Product ID'},
    yaxis={'title': 'Number of Items Sold'}
)

# Creating a Figure object by combining data and layout
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='top_10_products_bar_chart.html')
print("Bar chart saved as 'top_10_products_bar_chart.html'")






print("---Calculating item revenue---")
combined_orders_dataset['item_revenue'] = combined_orders_dataset['price'] + combined_orders_dataset['freight_value']
print( combined_orders_dataset['item_revenue'])

print("Calculating total revenue per seller.")
seller_revenue = combined_orders_dataset.groupby('seller_id')['item_revenue'].sum()
print(seller_revenue)

print("Identifying top 10 sellers by revenue.")
top_10_sellers_revenue = seller_revenue.sort_values(ascending=False).head(10)

print("\nTop 10 Sellers by Total Revenue:")
print(top_10_sellers_revenue)


# Extracting seller IDs (index) and revenue (values) for plotting
seller_ids = top_10_sellers_revenue.index.tolist()
revenue_values = top_10_sellers_revenue.values.tolist()

print("\nCreating bar chart for top 10 sellers by revenue using Plotly.")
# Creating a Bar trace using plotly.graph_objs (go)
data = [go.Bar(
    x=seller_ids,
    y=revenue_values
)]

# Defining layout for the plot sing plotly.graph_objs (go)
layout = go.Layout(
    title='Top 10 Sellers by Total Revenue',
    xaxis={'title': 'Seller ID'},
    yaxis={'title': 'Total Revenue'}
)

# Creating a Figure object  by combining data and layout
fig = go.Figure(data=data, layout=layout)

# Generating an interactive HTML plot file  using plotly.offline
pyo.plot(fig, filename='top_10_sellers_revenue_bar_chart.html')
print("Bar chart saved as 'top_10_sellers_revenue_bar_chart.html'")


required_cols = ['order_purchase_timestamp', 'price', 'freight_value']
print("Required columns:" + "" + str(required_cols))

item_revenue = combined_orders_dataset['item_revenue'] = combined_orders_dataset['price'] + combined_orders_dataset['freight_value']
print("Item Revenue: " + "" + str(item_revenue))

combined_orders_dataset['order_purchase_timestamp'] = pd.to_datetime(combined_orders_dataset['order_purchase_timestamp'])

#  Extracting Month: Extracting year and month into a 'YYYY-MM' format
combined_orders_dataset['order_month'] = combined_orders_dataset['order_purchase_timestamp'].dt.strftime('%Y-%m')

#  Grouping and Aggregating: Group by month and sum the item revenue [
monthly_revenue = combined_orders_dataset.groupby('order_month')['item_revenue'].sum().reset_index()
print("Monthly Revenue: " + " " + str(monthly_revenue))

#  Preparing Data for Chart: Extracting months and revenue for plotting
months = monthly_revenue['order_month']
revenue = monthly_revenue['item_revenue']

# Defining the trace for the line chart
trace = go.Scatter(
    x=months,
    y=revenue,
    mode='lines+markers',
    name='Monthly Revenue'
)

# Defining the layout for the chart
layout = go.Layout(
    title='Monthly Revenue Trend for Olist',
    xaxis=dict(title='Month (YYYY-MM)'),
    yaxis=dict(title='Total Revenue (Price + Freight)')
)

# Creating the figure object
fig = go.Figure(data=[trace], layout=layout)

# Saving the interactive chart as an HTML file
pyo.plot(fig, filename='olist_monthly_revenue_trend.html', auto_open=True)

print("Monthly revenue trend chart saved as 'olist_monthly_revenue_trend.html'")




