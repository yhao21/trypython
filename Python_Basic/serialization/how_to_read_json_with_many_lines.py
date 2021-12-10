import json


'''
If the json file contain many lines where each line is a dict, then you need to do this
'''



'''
dict_keys([
'creator',
'datePublished',
'docType',
'doi',
'id',
'identifier',
'isPartOf',
'issueNumber',
'language',
'outputFormat',
'pageCount',
'provider',
'publicationYear',
'publisher',
'sequence',
'tdmCategory',
'title',
'url',
'volumeNumber',
'wordCount',
'unigramCount',
'bigramCount',
'trigramCount'
])
'''

a = 0
with open('sample_jsonline.json', encoding='utf-8') as f:
    for line in f:
        '''
        now each line is a json dict
        '''
        json_line = json.loads(line)
        print(json_line['datePublished'])
        print(json_line.keys())
        # 2019-04-02
        # 2019-01-01
        # 2017-01-01

        for key, value in zip(list(json_line.keys()), list(json_line.values())):
            print(f'{key}            {value}')

        a += 1
        if a == 1:
            break

