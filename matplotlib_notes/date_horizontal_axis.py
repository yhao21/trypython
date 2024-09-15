

'''
Source code:
    https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html
    https://www.cnblogs.com/wreng/p/15195231.html




###------Prepare your data series for horizontal axis------###


The type of your x series can be datetime64 or string. Make sure you format the element
of your raw x series in this way: "2020-01-01".

Example


    x = df.iloc[:,0].values         # This is your time horizon. You MUST make sure that
                                      times are saved as datetime64 in your df, NOT str!
                                      Do not use .strftime('%Y-%M-%d') when you form your
                                      df!!!
    y = df[one_variable]            


    
###------Set specific interval for horizontal axis------###
    x = df.iloc[:,0].values         # This is your time horizon
    y = df[one_variable]            

    number_of_subplots = len(variables)
    fig, axs = plt.subplots(number_of_subplots, sharex = True, figsize = (25,10))

    fsize = 20          # fontsize
    index = 0

    for ax in axs:
        one_variable = variables[index]
        ax.plot(x,df[one_variable])    # Make sure you have you x series here!!!

        index += 1



        ###------If you want to use MONTH interval for horizontal axis------###
        ##fmt_half_year = mdates.MonthLocator(interval=6)   # You can choose a fix interval
        #fmt_half_year = mdates.MonthLocator([1,4,7,10])    # or a customized interval
        #ax.xaxis.set_major_locator(fmt_half_year)
        #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        #print(ax.xaxis.get_major_locator())


        ###------If you want to use YEAR interval for horizontal axis------###
        year_axis = mdates.YearLocator()
        ax.xaxis.set_major_locator(year_axis)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

        ###------Set labels------###
        ax.set_ylabel(one_variable, fontsize = fsize)
        ax.set_xlabel('Time', fontsize = fsize)

        ###------set fontsize for ticks on the horizontal and vertical axis------###
        ax.tick_params(axis = 'x', labelsize = fsize)  # Change the fontsize of x-axis
        ax.tick_params(axis = 'y', labelsize = fsize)  # Change the fontsize of x-axis



    fig.suptitle(title, fontsize = fsize)       # set the title for ALL subplots.
    fig.autofmt_xdate()         # 横轴显示过多时会自动旋转坐标值
    plt.savefig(png_path)


    
'''


