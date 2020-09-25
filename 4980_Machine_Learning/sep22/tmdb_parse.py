import json, os
import pandas as pd
import glob

if not os.path.exists('parsed_files'):
    os.mkdir('parsed_files')

df = pd.DataFrame()
for json_file_name in glob.glob('json_files/*.json'):



#json_file_name = os.path.join('json_files/tmdb550.json')

    f = open(json_file_name, "r")
    
    json_data = json.load(f)
    #print(json_data)
    
    
    df = df.append({
        'adult':json_data['adult'],
        'backdrop_path':json_data['backdrop_path'],
        'title':json_data['title']
        },ignore_index = True)

print(df)
