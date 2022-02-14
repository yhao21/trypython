


'''
https://api.etherscan.io/api
   ?module=stats
   &action=ethdailyprice
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken



You need to use send a http request using the url above to obtain data from the Etherscan

Example:

my_url ="https://api.etherscan.io/api + f'?module=stats&action=ethdailyprice&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey={YourApiKeyToken}'"
'''




import requests


#API_KEY = "V4TAKV1J5145DW4WXVVWH.....KAGT77RT2"
#url = "https://api.etherscan.io/api" + f"?module=stats&action=ethdailyprice&startdate=2019-02-01&enddate=2022-02-2&sort=asc&apikey={API_KEY}"
#
#r = requests.get(url)
#print(r.json())
#










