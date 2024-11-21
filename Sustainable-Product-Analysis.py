import pandas as pd
df = pd.read_csv("/content/Nykaa_Products_2023.csv")
df.head()

# Filter eco-friendly products
eco_keywords = ['eco-friendly', 'organic', 'natural', 'sustainable', 'green', 'biodegradable']
eco_friendly_products = df[df['Product Name'].str.contains('|'.join(eco_keywords), case=False, na=False)]

# Filter healthcare products
healthcare_keywords = ['health', 'wellness', 'medical', 'vitamin', 'supplement', 'skincare', 'hygiene']
healthcare_products = df[df['Product Name'].str.contains('|'.join(healthcare_keywords), case=False, na=False)]

# combined filtered words
combined_products = pd.concat([eco_friendly_products, healthcare_products])

# Save to a new CSV for further analysis
combined_products.to_csv('filtered_eco_health_products.csv', index=False)

# MARKET SHARE ANALYSIS
import matplotlib.pyplot as plt
import seaborn as sns

# Market Share Analysis
total_products = df.shape[0]
eco_health_count = combined_products.shape[0]
market_share = (eco_health_count / total_products) * 100

# Price Analysis
plt.figure(figsize=(12,6))
sns.histplot(combined_products['Original Price'], kde=True, color='green')
plt.title('Price Distribution of Eco-Friendly and Healthcare Products')
plt.xlabel('Product Price')
plt.ylabel('Frequency')
plt.show()

# Market share output
print(f"Market share of eco-friendly and healthcare products: {market_share:.2f}%")

# PRODUCT RATINGS & REVIEW ANALYSIS
# Rating Analysis
eco_friendly_avg_rating = pd.to_numeric(eco_friendly_products['Reviews'], errors='coerce').mean()
healthcare_avg_rating = pd.to_numeric(healthcare_products['Reviews'], errors='coerce').mean()

# Sentiment Analysis on Reviews (using TextBlob)
from textblob import TextBlob

def get_sentiment(review):
    analysis = TextBlob(str(review))
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

combined_products['Review Sentiment'] = combined_products['Reviews'].apply(get_sentiment)
sentiment_count = combined_products['Review Sentiment'].value_counts()

# Plot sentiment distribution
plt.figure(figsize=(10,5))
sentiment_count.plot(kind='bar', color='skyblue')
plt.title('Sentiment Distribution for Eco-Friendly and Healthcare Products')
plt.ylabel('Number of Reviews')
plt.xlabel('Sentiment')
plt.show()

# INVENTORY AND AVAILABILITY ANALYSIS
# Assuming products with zero reviews are considered 'low inventory' or 'out of stock'
out_of_stock = combined_products[combined_products['Reviews'] == 0].shape[0]
total_products_in_inventory = combined_products.shape[0]
out_of_stock_percentage = (out_of_stock / total_products_in_inventory) * 100

print(f"Out of stock percentage for eco-friendly and healthcare products based on reviews: {out_of_stock_percentage:.2f}%")

# Plot availability status based on reviews
review_status = combined_products['Reviews'].apply(lambda x: 'Out of Stock' if x == 0 else 'In Stock').value_counts()
plt.figure(figsize=(8,4))
review_status.plot(kind='bar', color='orange')
plt.title('Inventory Availability (Inferred from Reviews)')
plt.ylabel('Count')
plt.xlabel('Inventory Status')
plt.show()

# CUSTOMER REVIEW ANALYSIS
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Preprocess the review text for topic modeling
vectorizer = CountVectorizer(stop_words='english', max_features=1000)
X_reviews = vectorizer.fit_transform(combined_products['Reviews'].dropna())

# Applying LDA to find topics in reviews
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X_reviews)

# Displaying the top words for each topic
terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lda.components_):
    print(f"Topic {idx+1}:")
    print([terms[i] for i in topic.argsort()[-10:]])