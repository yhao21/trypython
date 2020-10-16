Date: 10/16/2020
Version: 1.0


================================================================================

CONTENTS:


Introduction.....................................................|introduction|
Arguments........................................................|arguments|
        URL list.................................................|url|
        Folder names.............................................|folder_names|
        File names...............................................|file_names|
        Scrapping method.........................................|method|
        Sleep time...............................................|sleep_mode|
Application and Examples.........................................|examples|

================================================================================

INTRODUCTION																								    *introduction*


This module can scrape one (or a list of) web page for you.
Call Scrapping(args).folder_setup() with arguments to process scrapping.

================================================================================

Arguments                                                       *arguments*


Url list                                                        *url*

Prepare the *url* in a list form even if you only have one url, otherwise the
program pops up with an error.

    Example:
    
    url = ['https://coinmarketcap.com/']
    or
    url = ['https://coinmarketcap.com/0/','https://coinmarketcap.com/1/']

--------------------------------------------------------------------------------

Folder names                                                    *folder_names*

The folder to store your html file is named by this argument. *folder_name*
should be a string.

    Example:
    
    folder_name = 'coin_html_file'

--------------------------------------------------------------------------------

File names                                                      *file_names*

Each html file being download is named by elements in *file_names*. 
file_names should be a list contains all file names for the html files.
Note, DO NOT contain file types in your file_name list, i.e., ".html".

    Examples:
    
    file_names = ['Page 1', 'Page 2', 'Page 3']

--------------------------------------------------------------------------------

Scrapping method                                                *method*

There are two methods to do web scrapping, i.e., requests or selenium.
The program scrapes website using requests by default. If the website is
asynchronous, you should set method = 'selenium' when you call the function.

    Examples:
    
    Scrapping(url, folder_names, file_names, method = 'selenium').folder_setup()

--------------------------------------------------------------------------------

Sleep time                                                      *sleep_mode*

The program has its default sleep time after scrapping each web page. 
It is defined by the sum of a random integer from 5 to 10 plus a random float
with normal distribution with mean = 8 and variance = 3.
If you do not want to use this default setting, set your own sleep time. It
should be a integer or float number.

    Examples:

		1. Sleep 5 seconds after downloading each pages.
		
		    sleep_time = 5
		    Scrapping(args, sleep_mode = sleep_time)

    2. Set a random sleep time though numpy
				sleep_time = numpy.random.randint(5,10) + numpy.random.normal(10,4)
		    Scrapping(args, sleep_mode = sleep_time)

--------------------------------------------------------------------------------

Application and Examples                                        *examples*


		import scrapping_module as sm

    url_base = 'https://coinmarketcap.com/'
    url = [url_base + str(i) + '/' for i in range(5)]
    folder_name = 'html_file'
    file_names = ['Page' + str(i) for i in range(len(url))]
    sm.Scrapping(url, folder_name, file_names, sleep_mode = 5).folder_setup()
















