import pandas as pd

# ~~~~~~~~~~~~~~~~~~~~~
# Create a list of date
# ~~~~~~~~~~~~~~~~~~~~~
"""
pd.date_range()

By default, it frequency is day("D")

a = pd.date_range(start = '2000-01-01', end = '2025-01-01')
    DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
                   ...
                   '2024-12-31', '2025-01-01'],
                  dtype='datetime64[ns]', length=9133, freq='D')
"""
a = pd.date_range(start = '2000-01-01', end = '2025-01-01')
print(a)
"""
Change frequency of time periods using `freq = `

    "D": day
    "M": month
    "Q": quarter
    "Y": year...

    You can also specify if you want the start or the end of period using "S", and "E", 
    e.g., "QS" will generate quarterly time and presented as the beginning of each quarter.

        DatetimeIndex(['2000-01-01', '2000-04-01', '2000-07-01', '2000-10-01',
                       ...
                       '2024-10-01', '2025-01-01'],
                      dtype='datetime64[ns]', length=101, freq='QS-JAN')
        
"""
a = pd.date_range(start = '2000-01-01', end = '2025-01-01', freq = 'QS')
print(a)







