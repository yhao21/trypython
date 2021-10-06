import pickle

with open('serialized_file_pickle.pkl', 'rb') as f:
    content = pickle.load(f)

print(content)