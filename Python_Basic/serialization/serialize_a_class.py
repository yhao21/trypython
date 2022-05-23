import pickle, json





class NewClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'My name is {self.name}. I am {self.age} years old.')



# serialize a class
se_class = pickle.dumps(NewClass)
print(se_class)


# load the class
load_class = pickle.loads(se_class)
a = load_class('Adam', 36)
a.show_info()

