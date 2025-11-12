"""
###------Alignment for df.to_html()------###

Convert df to html
    df.to_html(classes = ["PandasDataframe"])
Then in css file, write this
    
    .PandasDataframe td{
    		text-align: right;
    }

You must make sure the class is consistent





###------Format float number------###

Add commas to throusand place.

pd.options.display.float_format = "{:,}".format


"""
