import json


'''
If the json file contain many lines where each line is a dict, then you need to do this
'''



with open('sample_jsonline.json', encoding='utf-8') as f:
    for line in f:
        '''
        now each line is a json dict
        '''
        json_line = json.loads(line)
        print(json_line['datePublished'])
        # 2019-04-02
        # 2019-01-01
        # 2017-01-01

