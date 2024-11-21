# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the dataset
data = {
    'Date': ['2024-09-01', '2024-09-01', '2024-09-02', '2024-09-02', '2024-09-03', '2024-09-03', '2024-09-04', '2024-09-04', '2024-09-04', '2024-09-05'],
    'Product_ID': ['P1001', 'P1002', 'P1003', 'P1004', 'P1005', 'P1006', 'P1001', 'P1003', 'P1005', 'P1004'],
    'Category': ['Makeup', 'Makeup', 'Skincare', 'Hair Care', 'Skincare', 'Fragrance', 'Makeup', 'Skincare', 'Skincare', 'Hair Care'],
    'Units_Sold': [100, 80, 150, 120, 110, 50, 90, 200, 130, 140],
    'Revenue': [50000, 64000, 45000, 72000, 44000, 50000, 45000, 60000, 52000, 84000],
    'Discount (%)': [10, 20, 0, 0, 0, 10, 10, 0, 0, 0],
    'Price': [500, 800, 300, 600, 400, 1000, 500, 300, 400, 600],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'South', 'East', 'North', 'West']
}

# Convert 'Date' to datetime format
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot the sales trends
plt.figure(figsize=(14, 8))

# Subplot 1: Line plot for Units Sold over time
plt.subplot(2, 2, 1)
sns.lineplot(x='Date', y='Units_Sold', data=df, marker='o')
plt.title('Units Sold Over Time')
plt.xticks(rotation=45)
plt.ylabel('Units Sold')

# Subplot 2: Line plot for Revenue over time
plt.subplot(2, 2, 2)
sns.lineplot(x='Date', y='Revenue', data=df, marker='o', color='g')
plt.title('Revenue Over Time')
plt.xticks(rotation=45)
plt.ylabel('Revenue (INR)')

# Subplot 3: Bar plot for Units Sold by Region
plt.subplot(2, 2, 3)
sns.barplot(x='Region', y='Units_Sold', data=df, estimator=sum)
plt.title('Total Units Sold by Region')
plt.ylabel('Units Sold')

# Subplot 4: Bar plot for Revenue by Product Category
plt.subplot(2, 2, 4)
sns.barplot(x='Category', y='Revenue', data=df, estimator=sum)
plt.title('Total Revenue by Product Category')
plt.ylabel('Revenue (INR)')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
