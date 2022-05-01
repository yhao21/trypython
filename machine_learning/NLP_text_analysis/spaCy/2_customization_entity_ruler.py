import spacy, json


with open('full_tutorial/data/yelp_review.txt', 'r') as f:
    text = f.read().replace('\n', '')

nlp = spacy.load('en_core_web_lg')
text = 'KFC is a good place to eat fried chicken wings! Mr. Hao love it so much.'
doc = nlp(text)
print(doc)

print('\n\n-----------------------------------------------------------------------')


for ent in doc.ents:
    print(ent.text, ent.label_)


###------Entity Ruler------###
### Create your custom components. Add your own entity!!!

'''
In the text, KFC is recognized as an organization, but fried chicken wings can not be recognized.
If we want to add fried chicken wings to an entity called "Food", we need to do it by ourselves.

To do this we need to add a <entity_ruler> to the pipline.
'''
ruler = nlp.add_pipe('entity_ruler')
## Then check where is the entity in the entire pipline
current_pipe = nlp.analyze_pipes()
#print(current_pipe)
with open('current_pipeline.json', 'w') as g:
    json.dump(current_pipe, g)
'''
open json, in line 55, you can see <doc.ents> is under ner.
So, if the ner pipe cannot recognize "fried chicken wing", even if we add it to the 
entity, the machine still cannot label "fried chicken wing" as "Food"
Two methods to fix this:
    1. Give your ruler the ability to overwrite the ner
    2. put it before the ner before the pipeline!!! (let's do this)
'''

'''.
Here we ask the machine to label "fried chicken wing" as "Food"
Note:
    pattern is a list of dict.   Example:
    patterns = [
        {
            'label':'Food',
            'pattern':'tofu'
        },
        {
            'label':'Food',
            'pattern':'noodles'
        }
    ]

Let's create a new nlp obj to do this
'''
nlp1 = spacy.load('en_core_web_lg')

## here we pass an argument, let our ruler located before the ner pipe!!
ruler = nlp1.add_pipe("entity_ruler", before = 'ner') ## argument can be <before> <after>

patterns = [
        {
            'label':'Food',
            'pattern':'fried chicken wings' ## must make sure there is no typo!!
            }
        ]


ruler = ruler.add_patterns(patterns)
doc1 = nlp1(text)

for ent in doc1.ents:
    print(ent.text, ent.label_)

# Great!!!
# KFC ORG
# fried chicken wings Food
# Hao PERSON



'''
Now, Hao, rather Mr. Hao, is considered as PERSON. We want to add Mr. Hao to the pattern.
'''

print('\n\n-----------------------------------------------------------------------')
nlp2 = spacy.load('en_core_web_lg')
ruler = nlp2.add_pipe('entity_ruler', before = 'ner')
patterns = [
        {
            'label':'PERSON',
            'pattern': "Mr. Hao"
            },
        {
            'label':'Food',
            'pattern': "fried chicken wings"
            }
        ]
ruler = ruler.add_patterns(patterns)

# Note doc2 must be place after defining the ruler.
doc2 = nlp2(text)
for ent in doc2.ents:
    print('{:<30} {:<30}'.format(ent.text, ent.label_))

# Great!!
# KFC ORG
# fried chicken wings Food
# Mr. Hao PERSON



'''
Now we have another problem:
    A word can have different meaning. 
    For example, Mr. Deeds can be a name of a person, but it is also a name of a film.

    By using entity ruler, we can only define it as one kind of entity. 

    This problem is called "toponym resolution".


    Let's see if we can solve this using   Matcher


'''











