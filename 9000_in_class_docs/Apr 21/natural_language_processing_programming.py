import time
"""

why and how does Siri understand what you are talking about?



"""

import json
import pandas as pd
import string
import nltk
#nltk is a package to recognize natural language.


nltk.download('stopwords')


from nltk.corpus import stopwords
#stopwords 只is are之类的无实际意义的单词


from nltk.stem import WordNetLemmatizer
#this help you change the form of word, like 第三人称单数，单复数问题

from sklearn.feature_extraction.text import CountVectorizer
#countvectorizer把dataset转成一列一列的
from sklearn.naive_bayes import MultinomialNB

# nltk.download('stopwords')
# nltk.download('wordnet')

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score



review_text = []
review_stars = []


#使用with可以逐行读取，每一行是一个json。
with open('yelp_review_part.json', encoding='utf-8') as f:
    for line in f:
        json_line = json.loads(line)
        # print(json_line)
        review_text.append(json_line['text'])
        review_stars.append(json_line['stars'])
# print(review_stars)
# print(review_text)

dataset = pd.DataFrame(data={'text' : review_text, 'stars' : review_stars})
print(dataset)


dataset = dataset[(dataset['stars'] ==1) | (dataset['stars'] ==3) | (dataset['stars'] == 5)]

data = dataset['text']
target = dataset['stars']

lemmatizer = WordNetLemmatizer()

def pre_processing(text):
    text_processed = [char for char in text if char not in string.punctuation]
    text_processed = ''.join(text_processed)
    return [lemmatizer.lemmatize(word.lower()) for word in text_processed.split() if word.lower() not in stopwords.words('english')]

print(pre_processing('This is a test. This is a text processing program!!!'))

count_vectorize_transformer = CountVectorizer(analyzer=pre_processing).fit(data)
# print(count_vectorize_transformer.get_feature_names())

data = count_vectorize_transformer.transform(data)
# print(data.shape)
"""(7023, 22133)"""

data_training, data_test, target_training, target_test = train_test_split(data,target,test_size=0.25)

nb_machine = MultinomialNB()
nb_machine.fit(data_training,target_training)
# prediction = nb_machine.predict(data_test)

# print(confusion_matrix(target_test,prediction))
# print(accuracy_score(target_test,prediction))
"""[[ 304   39   23]
 [  40  122  108]
 [  47   48 1025]]
0.8263097949886105"""


text_review = "It's a horrible resturant. It's expensive!!!"
test_review_transformed = count_vectorize_transformer.transform([text_review])
prediction = nb_machine.predict(test_review_transformed)
prediction_prob = nb_machine.predict_proba(test_review_transformed)
print(prediction)
print(prediction_prob)


text_review = "baby shark do do do do do do ......"
test_review_transformed = count_vectorize_transformer.transform([text_review])
prediction = nb_machine.predict(test_review_transformed)
prediction_prob = nb_machine.predict_proba(test_review_transformed)
print(prediction)
print(prediction_prob)
"""
[1.]
[[0.65395365 0.308369   0.03767736]]
[5.]
[[0.07353804 0.11055511 0.81590685]]
"""
