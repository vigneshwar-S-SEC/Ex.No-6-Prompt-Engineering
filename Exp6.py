from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Simulated AI-generated text
generated_text = input("Enter the generated review text: ")
print("Generated Review:\n")
print(generated_text)

# Sentiment analysis
sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(generated_text)

print("\nSentiment Analysis:")
print(sentiment)

# Insight generation
if sentiment['compound'] >= 0.05:
    print("\nInsight: The review is positive and suitable for marketing promotion.")

elif sentiment['compound'] <= -0.05:
    print("\nInsight: The review is negative and may require improvement.")

else:
    print("\nInsight: The review is neutral.")