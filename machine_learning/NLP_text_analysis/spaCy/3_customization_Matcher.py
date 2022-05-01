import spacy
from spacy.matcher import Matcher



###------Define a matcher------###

content = "this is an email address: 12334@183.com"

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

pattern = [
        {"LIKE_EMAIL":True}
        ]

matcher.add('EMAIL_ADDRESS', [pattern])
doc = nlp(content)
matches = matcher(doc)
print(matches)

'''
Return:
(Match ID(hashed),  location pattern occur, location pattern end),     Match ID(string):EMAIL_ADDRESS
[(16571425990740197027, 6, 7)]

To show the token (word) is matched:
'''
match_id = matches[0][0]
match_id_string = nlp.vocab.strings[match_id]
print(match_id_string)    # EMAIL_ADDRESS

start = matches[0][1]
end = matches[0][2]
matched_word = doc[start:end]
print(matched_word)       #   12334@183.com



###------Use matcher to match a linguistic pattern------###





##------One Pattern------##
'''
Let's try to grab "imlicit goal" as one token.
It has the following patter: a ADJ + NOUN
'''
content = 'Their implicit goal was to understand how changes in society impacted the net utilities (also often called the welfare) of citizens in an attempt to design better societies.'



nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
doc = nlp(content)

pattern = [
        {"POS":"ADJ"},{"POS":"NOUN"}    # it says the pattern I need is a adj + noun, e.g., empirical paper, implicit goal
        ]
matcher.add('proper noun', [pattern])
matches = matcher(doc)
print(matches)
for matched_token in matches:
    start = matched_token[1]
    end = matched_token[2]
    span = doc[start:end]
    print(span)


#   implicit goal
#   net utilities
#   better societies




#------Greedy Search ------#
'''
we can add {'OP':"+"} to require the pattern to match 1 or more times
'''

nlp_new = spacy.load('en_core_web_sm')
matcher = Matcher(nlp_new.vocab)
doc = nlp_new(content)
print(doc)

for token in doc:
    print(token.pos_)

pattern = [
        {'POS':'ADV', 'OP':'+'}
        ]
matcher.add('my_matcher', [pattern])
matches = matcher(doc)
print(matches)

for token in matches:
    start = token[1]
    end = token[2]
    print(doc[start:end])

#  also
#  also often
#  often
'''
If we only add "OP":"+", it will find ADV or ADV+ADV
If we long need 'also often', pass greedy argument
'''

nlp_greedy = spacy.load('en_core_web_sm')
matcher = Matcher(nlp_greedy.vocab)
doc = nlp_greedy(content)

pattern = [
        {"POS":"ADV", 'OP':'+'}
        ]
matcher.add('my_matcher', [pattern], greedy = 'LONGEST')
matches = matcher(doc)
for token in matches:
    print(doc[token[1]:token[2]])

#  also often


'''
now we have another problem, 

matcher.add('my_matcher', [pattern], greedy = 'LONGEST')

the return of this matches is sorted by the length, from the longest to the shortest. But we don't need this. We want it to be sorted by the order of occurance in the text.


### sorted by length by default
#   great great great
#   awesome awesome awesome
#   good good
#   fantastic


But "fantastic" appears first, the order we want is 
#   fantastic
#   good good
#   great great great
#   awesome awesome awesome

Here we need .sort() and lambda

'''

content = 'fantastic game, good good study, great great great wow, hahaha, awesome awesome awesome'

nlp = spacy.load('en_core_web_sm')
doc = nlp(content)
matcher = Matcher(nlp.vocab)

pattern = [
        {'POS':'ADJ', 'OP':'+'}
        ]

matcher.add('my_matcher', [pattern], greedy = 'LONGEST')
matches = matcher(doc)
matches.sort(key = lambda x: x[1])
for match in matches:
    print(doc[match[1]:match[2]])
'''
Note, matches is a list contain many match, each match is a tuple (x in the lambda)
x[1] is the second element in each match, which is the start location of the match. This is what we want.
We want to sort the matches regard this.


return:

fantastic
good good
great great great
awesome awesome awesome


Done!
'''














###------More than one pattern------##
#
#'''
#To find more than one pattern, put each pattern into a list
#
#pattern = [
#        [pattern 1],
#        [pattern 2]
#        ]
#Note:
#    when you have more than one pattern, you don't need to put variable pattern into a list when you call <matcher.add>, e.g., matcher.add('id', pattern)
#'''
#pattern = [
#        [{"POS":"ADJ"}, {'POS':'NOUN'}],
#        [{"LOWER":'also'}, {'LOWER':'often'}, {'LOWER':'called'}]
#        ]
#
#matcher.add('two patterns', pattern)
#matches = matcher(doc)
#print(matches)
#
#for matched_token in matches:
#    start = matched_token[1]
#    end = matched_token[2]
#    span = doc[start:end]
#    print(span)
#
#
##   implicit goal
##   implicit goal
##   net utilities
##   net utilities
##   also often called
##   better societies
##   better societies
#
#
#
#
#
#
#
#
#
##------Practice: Find 'like noodles' or 'love bread '------#
#
#content = 'They really love bread for breakfast. And he also like noodles.'
#nlp = spacy.load('en_core_web_sm')
#doc = nlp(content)
#matcher = Matcher(nlp.vocab)
#
#
#
#pattern = [
#        {'LEMMA':{'IN':['like', 'love']}},
#        {'POS':'NOUN'}
#        ]
#matcher.add('my_matcher', [pattern])
#matches = matcher(doc)
#print(matches)
#
#for token in matches:
#    start = token[1]
#    end = token[2]
#    span = doc[start:end]
#    print(span)
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
#
#
