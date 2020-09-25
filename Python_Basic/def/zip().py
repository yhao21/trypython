import time



"""
zip可以把两个或多个列表拼接成一个列表，新列表里的元素以元组形式呈现

"""
name = ['adam','harry','bob','simon','paul']
age = [25,26,50,60,65]
occupation = ['phd','phd','Ta','Professor','Professor']
infos = zip(name,age,occupation)

for info in infos:
    print(info)

"""
return:
    ('adam', 25, 'phd')
    ('harry', 26, 'phd')
    ('bob', 50, 'Ta')
    ('simon', 60, 'Professor')
    ('paul', 65, 'Professor')
"""