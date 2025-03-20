#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]['label']

def comparative_sentiment_analysis(articles):
    sentiments = []
    for article in articles:
        sentiment = analyze_sentiment(article['title'])
        sentiments.append(sentiment)

    # Count sentiment distribution
    positive_count = sentiments.count("POSITIVE")
    negative_count = sentiments.count("NEGATIVE")
    neutral_count = sentiments.count("NEUTRAL")

    print("Sentiment Analysis Results:")
    print(f"Positive: {positive_count}")
    print(f"Negative: {negative_count}")
    print(f"Neutral: {neutral_count}")

    return {
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count,
        "sentiments": sentiments
    }

