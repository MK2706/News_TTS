import streamlit as st
import requests
from scrape_news import scrape_news
from sentiment_analysis import analyze_sentiment, comparative_sentiment_analysis
from summarization import summarize_text
from translation import translate_to_hindi
from text_to_speech import generate_tts
from keyword_extraction import extract_topics

# API base URL
API_URL = "http://localhost:8000"  

def main():
    # Set page title
    st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")

    # Sidebar input
    st.sidebar.title("News Analysis")
    company_name = st.sidebar.text_input("Enter company name (e.g., Tesla, Apple):")

    # Button to fetch news
    if st.sidebar.button("Fetch News"):
        st.session_state.articles = []
        st.session_state.sentiment_results = None

        articles = scrape_news(company_name)

        if articles:
            st.session_state.articles = articles
            st.session_state.sentiment_results = comparative_sentiment_analysis(articles)
            st.sidebar.success("Articles fetched successfully!")
        else:
            st.sidebar.error("No articles found.")

    # Main dashboard
    st.title("📊 News Summarization & Sentiment Analysis")

    if "articles" in st.session_state and st.session_state.articles:
        articles = st.session_state.articles
        sentiment_results = st.session_state.sentiment_results

        # Display sentiment metrics
        if sentiment_results:
            col1, col2, col3 = st.columns(3)
            col1.metric("📈 Positive Sentiment", f"{sentiment_results['positive']} articles")
            col2.metric("📉 Negative Sentiment", f"{sentiment_results['negative']} articles")
            col3.metric("⚖️ Neutral Sentiment", f"{sentiment_results['neutral']} articles")

        # Extract topics from all article titles
        article_titles = [article['title'] for article in articles]
        common_topics = extract_topics(article_titles)
        st.write("🔑 **Common Topics:**", ", ".join(common_topics))

        # Display articles
        for i, article in enumerate(articles):
            with st.expander(f"📰 {article['title']}"):
                st.write(f"**Source:** {article['source']}")
                st.write(f"[Read Full Article]({article['link']})")

                # Sentiment Analysis
                sentiment = analyze_sentiment(article['title'])
                st.write(f"**Sentiment:** {sentiment}")

                # Summarization
                summary = summarize_text(article['title'])
                st.write(f"**Summary:** {summary}")

                # Hindi Translation
                hindi_translation = translate_to_hindi(summary)
                st.write(f"**Translated Summary (Hindi):** {hindi_translation}")

                # Generate TTS
                if hindi_translation:
                    st.write("🎧 **Play Hindi Audio:**")
                    audio_file = generate_tts(hindi_translation)
                    st.audio(audio_file, format="audio/mp3")

if __name__ == "__main__":
    main()