Customer Behaviour Analysis


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the dataset
data = {
    'CUST_ID': ['C10001', 'C10002', 'C10003', 'C10004', 'C10005', 'C10006', 'C10007'],
    'BALANCE': [40.900749, 3202.467416, 2495.148862, 1666.670542, 817.714335, 1809.828751, 627.260806],
    'PURCHASES': [95.4, 0, 773.17, 1499, 16, 1333.28, 7091.01],
    'ONEOFF_PURCHASES': [0, 0, 773.17, 1499, 16, 0, 6402.63],
    'INSTALLMENTS_PURCHASES': [95.4, 0, 0, 0, 0, 1333.28, 688.38],
    'CASH_ADVANCE': [0, 6442.945483, 0, 205.788017, 0, 0, 0],
    'CREDIT_LIMIT': [1000, 7000, 7500, 7500, 1200, 1800, 13500],
    'PAYMENTS': [201.802084, 4103.032597, 622.066742, 0, 678.334763, 1400.05777, 6354.314328],
    'MINIMUM_PAYMENTS': [139.509787, 1072.340217, 627.284787, None, 244.791237, 2407.246035, 198.065894]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Set the figure size for the plots
plt.figure(figsize=(14, 8))

# Subplot 1: Bar plot for BALANCE
plt.subplot(2, 2, 1)
sns.barplot(x='CUST_ID', y='BALANCE', data=df)
plt.title('Customer Balance')
plt.ylabel('Balance')
plt.xticks(rotation=45)

# Subplot 2: Stacked bar plot for PURCHASES, ONEOFF_PURCHASES, INSTALLMENTS_PURCHASES
df_purchases = df[['CUST_ID', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES']].set_index('CUST_ID')
df_purchases.plot(kind='bar', stacked=True, ax=plt.subplot(2, 2, 2))
plt.title('Purchases Breakdown')
plt.ylabel('Amount')
plt.xticks(rotation=45)

# Subplot 3: Bar plot for CASH_ADVANCE
plt.subplot(2, 2, 3)
sns.barplot(x='CUST_ID', y='CASH_ADVANCE', data=df)
plt.title('Customer Cash Advances')
plt.ylabel('Cash Advance')
plt.xticks(rotation=45)

# Subplot 4: Bar plot for PAYMENTS
plt.subplot(2, 2, 4)
sns.barplot(x='CUST_ID', y='PAYMENTS', data=df)
plt.title('Customer Payments')
plt.ylabel('Payments')
plt.xticks(rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()