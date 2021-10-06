import pandas as pd
from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer



#df = pd.read_csv('airbnb-reviews-part.csv')
#print(df)

text_blob_obj = TextBlob('Tom is horrible! ML is great. Exam is difficult, but you guys will do well.')
#print(text_blob_obj)
#print(text_blob_obj.tags)
#print(text_blob_obj.tokens)
#print(text_blob_obj.words)
#print(text_blob_obj.sentences)


print(text_blob_obj.sentiment)
print(text_blob_obj.sentiment_assessments)
