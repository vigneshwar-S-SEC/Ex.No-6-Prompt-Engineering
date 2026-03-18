# Ex.No.6 Development of Python Code Compatible with Multiple AI Tools

## Aim: 

Write and implement Python code that integrates with multiple AI tools to automate the task of interacting with APIs, comparing outputs, and generating actionable insights with Multiple AI Tools.

## Explanation:

Develop a python code that integrates multiple AI tool by interacting with their APIs.
Compare outputs from different APIs.
Analyze the response and the Output.

The aim is to understand how to request help from AI tools for tasks like writing Python code, integrating with APIs, comparing outputs, and generating actionable insights.

## Code:

```
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Simulated AI-generated text
generated_text = input()

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
```

## Output:

[View The PDF](EXP6.pdf) 


## Result: 

The Python program was successfully executed to perform sentiment analysis on the input text.
The system accurately classified the sentiment as positive, negative, or neutral.
Thus, the objective of generating insights using AI tools was achieved successfully.
