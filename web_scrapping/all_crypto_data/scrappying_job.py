from data_scrappying import data_scrappying
import os
import pandas as pd







def each_crypto_scrappying():

    df = pd.read_csv(os.path.join('csv_folder', 'homepage_crypto_href.csv'))
    
    i = 1
    workload = len(df)
    for one_crypto in df.iloc[:,:].values:
        print(f'[{i}/{workload}]')
        file_name = one_crypto[0] + '.html'
        url = one_crypto[3]
        file_folder = 'each_crypto'
        
        if not os.path.exists(file_folder):
            os.mkdir(file_folder)
    
        data_scrappying(file_folder, file_name, url).check_file_existence()
        i += 1




def historical_data():
    df = pd.read_csv(os.path.join('csv_folder','each_crypto.csv'))

    file_folder = 'historical_data'
    if not os.path.exists(file_folder):
        os.mkdir(file_folder)
    i = 1
    workload = len(df)
    for one_crypto in df.iloc[:,:].values:
        name = one_crypto[0]
        print(f'[{i}/{workload}]')
        file_name = name + '.html'
        url = one_crypto[2]
        data_scrappying(file_folder, file_name, url).check_file_existence()


        i += 1





#each_crypto_scrappying()
historical_data()
