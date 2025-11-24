import pandas as pd

# ~~~~~~~~~~~~~~~~~~~~~
# Create a list of date
# ~~~~~~~~~~~~~~~~~~~~~
"""
###------1. Generate time series------###
[Function]: pd.date_range()

    By default, its frequency is day("D")
    
    [code]: 
        a = pd.date_range(start = '2000-01-01', end = '2025-01-01')

    [result]: 
        DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
                       ...
                       '2024-12-31', '2025-01-01'],
                      dtype='datetime64[ns]', length=9133, freq='D')

    ##------1.1 Change frequency------##
    Change frequency of time periods using `freq = `
        "D": day
        "M": month
        "Q": quarter
        "Y": year...


    You can also specify if you want the start or the end of period using "S", and "E", 
    e.g., "QS" will generate quarterly time and presented as the beginning of each quarter.

    [code]:
        a = pd.date_range(start = '2000-01-01', end = '2025-01-01', freq = 'QS')

    [result]:
        DatetimeIndex(['2000-01-01', '2000-04-01', '2000-07-01', '2000-10-01',
                           ...
                           '2024-10-01', '2025-01-01'],
                          dtype='datetime64[ns]', length=101, freq='QS-JAN')
            
----------------------------------------------------------------------------------------------------
###------2. Frequency conversion and resampling of time series------###
[Function]: df.resample()
    Note, time series column/index must frist be converted to datetime format using `pd.to_datetime`


    [code]:

        # create a df,
        t = pd.date_range(start = '2020-01-01', end = '2025-01-01', freq = 'MS')
        df = pd.DataFrame({'Time':t, 'value':[i for i in range(len(t))]})

        # set df index to be the Time column using set_index(), by default, it will drop Time col.
        df = df.set_index("Time")
        df = df.resample('QS').mean()

    [result]:
        raw df (monthly data):
                        value
            Time
            2020-01-01      0
            2020-02-01      1
            2020-03-01      2
            ...

        df after converting to quarterly data:
                        value
            Time
            2020-01-01    1.0
            2020-04-01    4.0
            2020-07-01    7.0
            ...


[Function]: df.resample(..., on = 'Col_name')
    Specify time series column to `on`.

    [code]:

        t = pd.date_range(start = '2020-01-01', end = '2025-01-01', freq = 'MS')
        df = pd.DataFrame({'Time':t, 'value':[i for i in range(len(t))]})
        df = df.resample('QS', on = 'Time').mean()
    [result]:
                    value
        Time
        2020-01-01    1.0
        2020-04-01    4.0
        2020-07-01    7.0
        ...
    

###------3. convert YYYY-MM-DD to YYYYQn------###
[Function]: pd.PeriodIndex(pd_series, freq = 'Q')

    [code]:
        t = pd.date_range(start = '2020-01-01', end = '2025-01-01', freq = 'MS')
        df = pd.DataFrame({'Time':t, 'value':[i for i in range(len(t))]})
        df['TimeQ'] = pd.PeriodIndex(df['Time'], freq = 'Q')
    [result]:

                 Time  value   TimeQ
        0  2020-01-01      0  2020Q1
        1  2020-02-01      1  2020Q1
        2  2020-03-01      2  2020Q1
    
            
"""






