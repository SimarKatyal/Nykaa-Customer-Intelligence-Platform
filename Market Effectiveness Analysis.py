# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataset
data = {
    'Campaign_ID': ['C1001', 'C1002', 'C1003', 'C1004', 'C1005', 'C1006'],
    'Date': ['2024-09-01', '2024-09-02', '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-06'],
    'Campaign_Type': ['Social Media', 'Influencer', 'Paid Ads', 'Email Marketing', 'Social Media', 'Paid Ads'],
    'Impressions': [100000, 80000, 120000, 60000, 110000, 90000],
    'Clicks': [5000, 4000, 7000, 3000, 6000, 5500],
    'Conversions': [300, 200, 500, 150, 400, 350],
    'Conversion_Rate (%)': [6, 5, 7.14, 5, 6.67, 6.36],
    'Revenue': [600000, 400000, 1000000, 300000, 800000, 700000],
    'Spend': [50000, 45000, 70000, 20000, 60000, 55000],
    'ROI': [12.0, 8.89, 14.3, 15.0, 13.33, 12.73]
}

# Convert 'Date' to datetime
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plotting the charts
plt.figure(figsize=(14, 10))

# Subplot 1: Bar plot for Revenue by Campaign Type
plt.subplot(2, 2, 1)
sns.barplot(x='Campaign_Type', y='Revenue', data=df, estimator=sum)
plt.title('Revenue by Campaign Type')
plt.xticks(rotation=45)
plt.ylabel('Revenue (INR)')

# Subplot 2: Bar plot for ROI by Campaign Type
plt.subplot(2, 2, 2)
sns.barplot(x='Campaign_Type', y='ROI', data=df, estimator=sum)
plt.title('ROI by Campaign Type')
plt.xticks(rotation=45)
plt.ylabel('ROI')

# Subplot 3: Line plot for Clicks and Conversions over Time
plt.subplot(2, 2, 3)
sns.lineplot(x='Date', y='Clicks', data=df, marker='o', label='Clicks', color='b')
sns.lineplot(x='Date', y='Conversions', data=df, marker='o', label='Conversions', color='g')
plt.title('Clicks and Conversions Over Time')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()

# Subplot 4: Line plot for Revenue and Spend over Time
plt.subplot(2, 2, 4)
sns.lineplot(x='Date', y='Revenue', data=df, marker='o', label='Revenue', color='g')
sns.lineplot(x='Date', y='Spend', data=df, marker='o', label='Spend', color='r')
plt.title('Revenue and Spend Over Time')
plt.ylabel('INR')
plt.xticks(rotation=45)
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
