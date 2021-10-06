

Date: May 5, 2020

Version: 1.0






Information:

1. This module will do web scrapping through requests. 

2. This module will remind you how many pages have downloaded and time left.





Instruction:

	parameters:
		
		url: user need to submit Url to this module. Url should be in list form!
		
		file name: user need to name the web page he/she has downloaded. The file name should be in list form!

		folder name: user need to name the folder used to save html pages. Folder name should be a string!

		method: in which method you would like to scrap the web page (requests or selenium). Default value is 'requests'. If you would like to change, input 'selenium'.

	
	Example:

		from my_scrapping.scrapping import Scrapping

		base_url = 'https://coinmarketcap.com/rankings/exchanges/'

    		url = [base_url + str(i) + '/' for i in range(1,6)]

    		folder_name = 'main page'

    		file_name = ['page ' + str(i) for i in range(1, len(url) + 1)]

    		Scrapping(url, file_name, folder_name, 'selenium').folder_setup()




