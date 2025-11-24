import pandas as pd




'''
###------1. Use a column as index------###
    ###------method 1------###
    df.index = [a list of items]
    ###------method 2------###
    df = df.set_index('target_column')

        This function will set the index of df to be the `target_column`, and drop the `target_column`.

'''
