import pandas as pd


'''
split the entire dataset into several small datasets.
(use get_chunk!!!)

run for loop parsing each small dataset.

'''

###------Step 1: split the entire dataset into many small datasets------###

path_base = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
path_csv = os.path.join(path_base, 'data', 'data_csv', 'data_tx_info_6-0.csv')
df = pd.read_csv(path_csv, iterator = True)

'''
      block_number  block_date block_time  ... tx_type  tx_gas  tx_gasPrice
   0      13081215  2021-08-23   11:15:04  ...       2  300000  33712396791
   
   [1 rows x 9 columns]
'''


csv_dir = './my_data'
Path(csv_dir).mkdir(exist_ok = True)

i = 0
for one_df in df:

    #   the value in column "block_number" in the first row
    start = str(one_df['block_number'].values[0])
    #   the value in column "block_number" in the last row
    end = str(one_df['block_number'].values[-1])
    print(start)

    csv_path = os.path.join(csv_dir, f'{str(i)}_{start}-{end}.csv')
    one_df.to_csv(csv_path)

    i += 1


###------Step 2: get the data you need from iterating each df------###
##  This will occupy only a very small amount of memory.
##  Remember to comment step 1. You don't need that large dataset.


csv_dir = './my_data'


counts = pd.Series(dtype=int)
for one_file in glob.glob(os.path.join(csv_dir, '*.csv')):
    df = pd.read_csv(one_file)
    counts = counts.add(df['from'].value_counts(), fill_value = 0)
    counts = counts.add(df['to'].value_counts(), fill_value = 0)
    print(one_file)

    
print(counts)
