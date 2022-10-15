'''

Method 1:


    sudo python3.8 -m pip install fastparquet
    
    
    save your dataframe into <parquet> format, instead of csv.
    It will save you much more disk space.
    
    
    144MB csv -----> 60.5MB parquet
    
    
    
        df.to_parquet(<path_to_parquet_file>)


        df.read_parquet(<path_to_parquet_file>)




Method 2:
    Save to feather
'''

