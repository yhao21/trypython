



data = {
        "name":"Adam",
        "age":40
        }

# ~~~~~~~~~~~~~~~~~~~~~~~
# Get each key:value pair using for loop
# ~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~
# .items()
# ~~~~~~~~~~~~~~~~~~~~~~~
print(data) # {'name': 'Adam', 'age': 40}
print(data.items()) # dict_items([('name', 'Adam'), ('age', 40)])

###------Get key-value paring using for loop------###
for i in data.items():
    print(i)
    """
    Result:
        ('name', 'Adam')
        ('age', 40)
    You will only get the key if you use:
        for i in data:
            print(i)
    """
for (key, value) in data.items():
    print(f"{key} -> {value}")
    """
    Result:
        name -> Adam
        age -> 40
    """

for index, item in enumerate(data.items()):
    print(f"{index} -> {item}")
    """
    Result:
        0 -> ('name', 'Adam')
        1 -> ('age', 40)
    """
# You can make it even more clear
for index, (key, values) in enumerate(data.items()):
    print(f"{index} -> {key} -> {values}")
    """
    Result
        0 -> name -> Adam
        1 -> age -> 40
    You need to use `index, (key, values)` not `index, key, values`.
    """
