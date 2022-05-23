import json




a = ['a', 'b', 'c']
a.remove('a')
print(a)


keys = []
with open('sample_jsonline.json') as f:
    a = 0
    for line in f:
        json_line = json.loads(line)
        keys_list = list(json_line.keys())
        print(len(keys_list))
        if a == 0:
            keys = keys_list
        else:
            for item in keys:
                if item not in keys_list:
                    keys.remove(item)
print(keys)
print(len(keys))

        





