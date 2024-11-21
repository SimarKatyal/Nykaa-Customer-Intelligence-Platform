Product Performance Analysis

# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the dataset
data = {
    'Product_ID': ['P1001', 'P1002', 'P1003', 'P1004', 'P1005', 'P1006'],
    'Product_Name': ['Nykaa Lipstick', 'Nykaa Foundation', 'Nykaa Face Wash', 'Nykaa Shampoo', 'Nykaa Moisturizer', 'Nykaa Perfume'],
    'Category': ['Makeup', 'Makeup', 'Skincare', 'Hair Care', 'Skincare', 'Fragrance'],
    'Price': [500, 800, 300, 600, 400, 1000],
    'Units_Sold': [1500, 1200, 3000, 2500, 2000, 500],
    'Revenue': [750000, 960000, 900000, 1500000, 800000, 500000],
    'Avg_Rating': [4.5, 4.2, 4.8, 4.1, 4.3, 4.7],
    'Returns': [50, 30, 20, 40, 10, 5],
    'Stock_Level': [200, 100, 50, 150, 300, 75]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Plotting the charts
plt.figure(figsize=(14, 8))

# Subplot 1: Bar plot for Revenue
plt.subplot(2, 2, 1)
sns.barplot(x='Product_Name', y='Revenue', data=df)
plt.title('Revenue per Product')
plt.ylabel('Revenue (INR)')
plt.xticks(rotation=45)

# Subplot 2: Bar plot for Units Sold
plt.subplot(2, 2, 2)
sns.barplot(x='Product_Name', y='Units_Sold', data=df)
plt.title('Units Sold per Product')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)

# Subplot 3: Bar plot for Average Rating
plt.subplot(2, 2, 3)
sns.barplot(x='Product_Name', y='Avg_Rating', data=df)
plt.title('Average Rating per Product')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)

# Subplot 4: Bar plot for Returns
plt.subplot(2, 2, 4)
sns.barplot(x='Product_Name', y='Returns', data=df)
plt.title('Product Returns')
plt.ylabel('Returns')
plt.xticks(rotation=45)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()