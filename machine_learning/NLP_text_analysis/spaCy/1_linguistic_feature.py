import spacy


###------Lemmatization------###

content = 'The utility function measures the happiness of consumer while consuming a certain consumption bundle.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(content)


print('\n\n------------------------------------------------------------------')
print(doc)

# load lemmatizer
lemmatizer = nlp.get_pipe('lemmatizer')
lemma_result = [token.lemma_ for token in doc]
print(lemma_result)
#       The utility function measures the happiness of consumer while consuming a certain consumption bundle.
#       ['the', 'utility', 'function', 'measure', 'the', 'happiness', 'of', 'consumer', 'while', 'consume', 'a', 'certain', 'consumption', 'bundle', '.']





###------Noun chunks------###
'''
Noun chunks are "base noun phrases", e.g., a noun plus the words describing the noun.
'''

print(list(doc.noun_chunks))
#       [The utility function, the happiness, consumer, a certain consumption bundle]





###------Work on a list of txt------###
content = [
        "this is an apple",
        "this is an orange",
        ]


doc1 = nlp.pipe(content)
for one_doc in doc1:
    print(one_doc)


#   There are two one_doc:
#       this is an apple
#       this is an orange


