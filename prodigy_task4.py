# -*- coding: utf-8 -*-
"""Prodigy-Task4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uTABWHfFOEXKM9zRrz7sTTLMFUPmUohg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("twitter_training.csv")

df.head()

df.isnull().sum()

df.describe()

df.dtypes

# prompt: add title row, names of each column should be ID, Brand Name, Status, Response

new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = ['ID', 'Brand Name', 'Status', 'Response'] #set the header row as the df header
df.head()

# Remove duplicates if necessary
df.drop_duplicates(inplace=True)

from textblob import TextBlob

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Apply the function
df['calculated_sentiment'] = df['Status'].apply(get_sentiment)

# Check distribution of sentiment
df['calculated_sentiment'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

# Sentiment distribution
sns.countplot(x='calculated_sentiment', data=df)
plt.title('Sentiment Distribution')
plt.show()

# Group by brand and sentiment to see trends
sentiment_trend = df.groupby([df['Brand Name'], 'calculated_sentiment']).size().unstack()

# Plot sentiment trend over time
sentiment_trend.plot(kind='line', figsize=(12,6))
plt.title('Sentiment Trend Over Brand')
plt.ylabel('Tweet Count')
plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Generate word clouds for each sentiment
def generate_wordcloud(sentiment):
    # Adjust the column names based on the dataset
    # Filter for the desired sentiment and select the 'Response' column
    responses = df[df['calculated_sentiment'] == sentiment]['Response']

    # Convert all elements in 'responses' to strings
    text = ' '.join(str(response) for response in responses)

    # Create the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {sentiment.capitalize()} Responses')
    plt.show()

# Generate word clouds for Positive, Negative, and Neutral sentiments
generate_wordcloud('positive') # Updated to match the sentiment values from get_sentiment function
generate_wordcloud('negative') # Updated to match the sentiment values from get_sentiment function
generate_wordcloud('neutral')  # Updated to match the sentiment values from get_sentiment function

