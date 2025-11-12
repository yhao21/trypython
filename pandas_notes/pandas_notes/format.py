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


###------Change fontsize for df.to_html()------###
You can manually use a <div> tag to wrap it up.

df_latest = df.to_html()
df_latest = f"<div style='font-size: 20px;'>{df_latest}</div>"
"""
