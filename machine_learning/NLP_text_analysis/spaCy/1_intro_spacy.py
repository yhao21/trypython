
'''
download spacy and model

    sudo pip3.8 install spacy
    sudo 
    sudo python3.8 -m spacy download en_core_web_sm          # a small english model  (efficient)
    sudo python3.8 -m spacy download en_core_web_md          # medium model (contain word vectors)
    sudo python3.8 -m spacy download en_core_web_lg          # large model (contain word vectors)
    sudo python3.8 -m spacy download en_core_web_trf          # an accurate english model  (accurate)

Note: 
    sm and trf piplines have no static word vectors!!



### md and trf can run ent.label_, sm cannot



text = Service is good and all I'm just concerned about having...

Create a doc obj:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

Doc obj is different with text. 
    Doc obj counted in individual token, e.g., words, punctuations, ...
    it separates text to small pieces. To check it:
    for token in doc:
        print(token)

    Return:
        Service
        is
        good
        and
        all
        I
        'm
        just
        concerned
        about


### 
Split in sentence:
    doc.sents     return sentences from a text

    for sent in doc.sents:
        print(sent)


        Return:
            Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary?
            How that patient's privacy is respected?
            I don't understand.
            When they ask you to get naked and cover yourself with a piece of cloth are there security guys watching the show?
    

    !!! Note, <doc.sents> returns a generator obj, so you cannot use <doc.sents[i]> to grab the ith sentence.
    You need to convert it to a list, then grab the ith sentence.





### 

SpaCy always return an obj, not a single string


sentence1 = list(doc.sents)[0]
    return:  sentence: Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary?


token2 = sentence1[1]        it will return the second word in the sentence
    return: is




### 

Change types:
(Attributes of a spacy obj)


Now sentence1 is a spacy obj. If you want to convert it to a string:

    a = sentence1
    print(type(a))            <class 'str'>




The word/punctuations on the very left (the begining of this sentence):
    sentence1 = list(doc.sents)[0]        Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary?
    token2 = sentence1[1]                 is

    What is the word on the left side of 'is'?

    left_word = token2.left_edge          Service



The word/punctuations on the very right (the end of this sentence):
    end_word = token2.right_edge          ?



!!! Note, spacy encode strings to hash values to reduce memory usage. You need to add "_" behind the varible to show string

    print(token2.lemma_)    be
    print(token2.lemma)     10382539506755952630
    
    more details about the attributes:
    https://spacy.io/api/token#attributes
    

###
    Useful attributes:
    .text       convert to string
    .pos_       return part of speech(POS), e.g., verb, proper noun (PROPN), noun, punctuation(PUNCT),...
    .dep_       return dependency relation
    .label_     return entity label, 
                GPE: geographical political entity, e.g., The united states of america
                LOC: location, e.g., North America
                CARDINAL: cardinal number, e.g., 50
                NORP: national or religious political entity, e.g., Indian
                DATE:
                EVENT: the American Revolutionary War


    
    for token in sentence1:
        print(f'{token.text}      {token.pos_}       {token.dep_}')


###
    To visualize relationship between words
    from spacy import displacy


###  Named entity recognation(NER)
    return each entity and its type:

        for ent in doc.ents:
            print(ent.text, ent.label_)
        


### Word Vectors

Purpose of this is to let computer understand the word (in vector form, i.e., numbers)

## You must download and load en_core_web_md model! not other models






'''

import numpy as np
import spacy
#from spacy import displacy





text = "Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary? How that patient's privacy is respected? I don't understand. When they ask you to get naked and cover yourself with a piece of cloth are there security guys watching the show? OMG this is wrong in so many levels... This is a HIPAA violation. Cameras can't be installed on exam rooms. It is called A.B."



# it returns an object
#en_core_web_trf
nlp = spacy.load('en_core_web_md')


doc = nlp(text)
#print(doc)

## split text into words and punctuations.
#for token in doc:
#    print(token)
#
#
## split text into sentences
#for sent in doc.sents:
#    print(sent)

## doc.sents return a generator, we need to convert it to a list first.
#sentence1 = list(doc.sents)[0]
#print(f'sentence: {sentence1}')
#
#
#token2 = sentence1[1]
#print(type(sentence1))
#
#a = sentence1.text
#print(type(a))
#
#left_word = token2.right_edge
#print(left_word)
#
#print(token2.lemma_)    
#print(token2.lemma)     
#
#
#print(sentence1)
#for token in sentence1:
#    print(f'{token.text}      {token.pos_}       {token.dep_}')


#print(doc)
for ent in doc.ents:
    print(ent.label_)
#
#=========================



#=========================
# Word Vector
#=========================
### You must download and load en_core_web_md model! not other models
#
#
#
#sentence1 = list(doc.sents)[0]
#print(sentence1)
#
####---### Generate similar words
#
## step 1, create your word
#your_word = "good"
#
## step 2, map it to hash value
## this will map "good" to a hash value
#hash_string =nlp.vocab.strings[your_word] 
#
## step 3, create word vector, return a ndarray and you need to put it into a []
#word_vector = nlp.vocab.vectors[hash_string]
#word_vector = np.asarray([word_vector])
#
## step 4, you can find words similiar to your word in the text. ms for most similar
## need to say claim how many similar words is need
## return a list of ndarrays
#ms = nlp.vocab.vectors.most_similar(word_vector, n = 10)
## use .strings[]  to show these words
##for i in ms:
##    print(i)
##    returns:
##
##        #[[11653038090416493029  5711639017775284443]]
##        #[[6441   90]]
##        #[[1. 1.]]
#
#
#
### ms[0][0] is [11653038090416493029  5711639017775284443]
#words = [nlp.vocab.strings[w] for w in ms[0][0]]
#print(words)
### ['gOOD', 'good', 'Good', 'greAt', 'Great', 'great', 'Better', 'better', 'betteR', 'Very']
#


###---### Compare the similarity of two texts


doc1 = nlp('You are awesome')
doc2 = nlp('You are great')


similarity = doc1.similarity(doc2)
print(similarity) ## 0.9539167414217083 They are quite the same!!












