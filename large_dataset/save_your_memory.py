###------Save memory when generating df within a loop------###

'''
      def extract_data():
          pass
      
      for i in range(10):
          tx_info = extract_data()
          df = pd.DataFrame(tx_info, columns = ['block_number', 'block_miner'])
      
          # idenity specific dtype for each columns
          dtypes = {
                  'block_miner':'category',
                  'block_number':'int32'
                  }
      
          df = df.astype(dtypes, copy = False)
          df.drop_duplicates(inplace = True)
      
          df.to_csv('dataset.csv', index = False)
      
          del df, tx_info
    

    Always del df and tx_info after you save it to csv. Save your memory.
    Always idenity specific dtype after you generate df.
'''
