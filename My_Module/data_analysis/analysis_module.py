import pandas as pd





class DataClean():

    def __init__(self, coin_df, gecko_df, mark = 'repetition'):
        self.coin_rep = None
        self.gecko_rep = None
        self.coin_df = coin_df
        self.gecko_df = gecko_df
        self.mark = mark
        self.delete_rows = []

    def get_repetition(self):
        '''
        This function sort df based on self.mark, i.e., repetition by default
        If you need to sort by other item, assign str to mark.
        '''

        self.coin_df = self.coin_df.sort_values(self.mark).reset_index(drop = True)
        self.gecko_df = self.gecko_df.sort_values(self.mark).reset_index(drop = True)

        # rep = [1,2,3,4,....192]
        self.coin_rep = list(self.coin_df.iloc[:, 1].values)
        self.gecko_rep = list(self.gecko_df.iloc[:, 1].values)
        #print(self.coin_rep)


    def remove_rows(self):
        '''
        Compile rows need to delete (based on self.mark).
        '''

        self.get_repetition()

        for item in self.coin_rep:
            if not item in self.gecko_rep:
                # coin_df need to delete row with 'item'
                self.delete_rows.append(('coin', item))
        for item in self.gecko_rep:
            if not item in self.coin_rep:
                self.delete_rows.append(('gecko', item))
        #print(self.delete_rows)


    def clean_rows(self):
        '''
        Delete rows that appears only in one df.
        We need to make sure both dfs have same rows and comparable data.
        Example:
        df_a = [
            [round, name, price],
            [1, aaa, 100],
            [2, bbb, 200],
            [5, eee, 500],
            ]
        df_b = [
            [round, name, price], 
            [1, aaa, 100],
            [2, bbb, 200],
            [3, ccc, 300],
            ]

        df_a has round = 5 but don't have round = 3
        df_b has round = 3 but don't have round = 5

        Hence, we don't need round = 3 and round = 5 in both df.
        We only need round = 1 and 2.

        This function will delete round 3 and 5 for you.
        '''

        self.remove_rows()
        # self.delete_rows = [('gecko', 149), ('gecko', 190)]
        # it will delete row with repetition = 149 in self.gecko_df
        for row in self.delete_rows:
            #print(row[0])
            if row[0] == 'gecko':
                # get row indexing with repetition == 149
                row_index = self.gecko_df[self.gecko_df['repetition'] == row[1]].index.values[0]
                self.gecko_df = self.gecko_df.drop(self.gecko_df.index[row_index])
                # reset index after delete any row
                self.gecko_df = self.gecko_df.sort_values('repetition').reset_index(drop = True)
                #print('\n\n')
                #print(self.gecko_df[self.gecko_df['repetition'] == row[1]])
                #print('len: gecko_df : ', len(self.gecko_df))
            if row[0] == 'coin':
                row_index = self.coin_df[self.coin_df['repetition'] == row[1]].index.values[0]
                self.coin_df = self.coin_df.drop(self.coin_df.index[row_index])
                # reset index after delete any row
                self.coin_df = self.coin_df.sort_values('repetition').reset_index(drop = True)
                #print('\n\n')
                #print(self.coin_df[self.coin_df['repetition'] == row[1]])
                #print('len: coin_df :', len(coin_df))

        print(len(self.coin_df))
        print(len(self.gecko_df))
        return self.coin_df, self.gecko_df





    



if __name__ == '__main__':

    coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
    gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
    
    coin_bitcoin = coin_df[coin_df['name'] == 'bitcoin']
    gecko_bitcoin = gecko_df[gecko_df['name'] == 'bitcoin']

    coin_clean, gecko_clean = DataClean(coin_bitcoin, gecko_bitcoin).clean_rows()

