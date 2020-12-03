import pickle



original_obj = list(range(100))

print(original_obj)

#a = pickle.dumps(original_obj)
#print(a)

'''
if we directly save original_obj into a file, it will become string rather
an array.
'''


## save it to a pickle file
#with open('serialized_file.pickle','wb') as f:
#    pickle.dump(original_obj, f)



### Load the file, it is still a series
with open('serialized_file.pickle', 'rb') as g:
    html = pickle.load(g)

print(html)
print(type(html))

