import spacy, os
import textacy







# remember to replace \n if you copy reviews directly from the website.
# so that you can can make it really looks like a 'sentence'.
with open('data/yelp_review.txt', 'r') as f:
    text = f.read().replace('\n', '')




#spacy.prefer_gpu()
nlp = spacy.load('en_core_web_lg')
doc = nlp(text)
print('\n\n----------------------------------------------------------------------------------------')

####------sentence recognization------###
sentences = list(doc.sents)
#print(sentences[2])
#for sent in sentences:
#    print(sent)
#
#
#
#
####------NER named entity recognization------###
#ents = list(doc.ents)
#for ent in ents:
#    print(ent, ent.label_)
#
#
#
#
#
####------Tokenization------###
#
## tokenize a sentence, token: a work, a punctuation, etc.
#
#sentence = sentences[1]
#for token in sentence:
#    print(token.text, token.pos_)
#
#
#
###------.right_edge------##
##Find the last word in a sentence
#sentence1 = sentences[0]
#print(sentence1)
## SO cute/pretty inside, can't wait to see this place in the summer with the doors all open.
#
#one_token = sentence1[1]
#last_word = one_token.right_edge
#print(one_token)      #cute
#print(last_word)      #/
#


##------lemmatization------##
sentence1 = sentences[1][:5]
for token in sentence1:
    print(token, token.lemma_)

## Return:
    #Parking parking
    #nearby nearby
    #is be
    #easy easy
    #and and
    
    




#
###------noun_chunks------##
#
## if we want to grab nouns:
#
#nouns = []
#verb = []
#for sentence in sentences:
#    for token in sentence:
#        if token.pos_ == 'NOUN':
#            nouns.append(token.text)
#
#print(nouns)
#
#
## A built-in method:
## it will grab noun phrase, instead of just noun itself.
#chunks = list(doc.noun_chunks)
#for chunk in chunks:
#    if 'food' in chunk.text:
#        print(chunk)
#
#
###------Verb------##
#
#patterns = [
#        {"POS":"ADV"},
#        {"POS":"VERB"}
#        ]
#
##verb_phrases = textacy.extract.matches.token_matches(doc, pattern = patterns)
#verb = []
#for sentence in sentences:
#    for token in sentence:
#        if token.pos_ == 'VERB':
#            verb.append(token.text)
#
#print(verb)
#
#
#
#
#
#
#
#
#
#
