import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

df = pd.read_csv('airbnb-reviews-part.csv', sep = ';')
print(df)


comment_list = df.iloc[0:500, 5].values


comment = TextBlob(comment_list[0], analyzer=NaiveBayesAnalyzer())

print(comment)
print(comment.sentiment)
'''
The host canceled this reservation 54 days before arrival. This is an automated posting.
Sentiment(classification='neg', p_pos=0.2918114729915541, p_neg=0.7081885270084473)
'''
