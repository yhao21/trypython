import pickle

original_object = 'Baby shark doo doo doo doo doo doo'

print(original_object)

with open('serialized_file_pickle.pkl', 'wb') as f:
    pickle.dump(original_object, f)

"""
pickle make your file size smaller.
"""

"""
for machine learning,
you do not need to fit the model every time you run the program.
you can save the machine into a pickle file.

then you can send the machine to someone else.

"""