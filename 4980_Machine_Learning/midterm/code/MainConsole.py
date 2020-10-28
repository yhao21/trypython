import os, glob
from scrapping_module import Scrapping, DeepLink, merge_rating_links
from parsing_module import Parsing
from scrapping_module import name_extraction as etr
from deeplink_parsing import ParsingDeepLink



#==============================================================================
# Step 1. Download 48hr data
#==============================================================================

#url_coin_base = 'https://coinmarketcap.com/' 
#url_gecko_base = 'https://www.coingecko.com/en?page=' 
#url_list = [(url_coin_base + str(i), url_gecko_base + str(i)) for i in range(1,6)]
#folder_name = ['coinmktcap_html_file', 'gecko_html_file']
#Scrapping(url_list, folder_name, 0.25).folder_setup()


#==============================================================================
# Step 2. Parsing data and deeplink
#==============================================================================

#folder = 'coinmktcap_html_file'
#coinmkt_parse_and_deeplink = Parsing(folder).parsing_coin_html()
#folder = 'gecko_html_file'
#gecko_parse_and_deeplink = Parsing(folder).parsing_gecko_html()
### pairing urls for last step scrapping
### i.e., [(coin_url, gecko_url), (coin_url, gecko_url)...]
#deeplink_list = [(coin, gecko) for coin, gecko in zip(coinmkt_parse_and_deeplink, gecko_parse_and_deeplink)]
#
#print('=' * 100 + '\nFinish pairing' + ' [ ' + str(len(deeplink_list)) + ' ] ' + 'URLs...\n' + '=' * 100)
#
#file_names = etr(deeplink_list)




#==============================================================================
# Step 3. Scrapping 500 coins deeplink info
#==============================================================================

#####test
#deeplink_list = [('https://coinmarketcap.com/currencies/bitcoin','https://www.coingecko.com/en/coins/bitcoin'),('https://coinmarketcap.com/currencies/ethereum','https://www.coingecko.com/en/coins/ethereum'),('https://coinmarketcap.com/currencies/tether','https://www.coingecko.com/en/coins/tether')]
#
#file_names = etr(deeplink_list)
#print(len(file_names))
####test

#deeplink_folder = ['coin_500deeplink', 'gecko_500deeplink']
### Then you can call scrapping module
### 0.25 for 15 mins. Recall, for loop repeat every 15 mins, and unit of 0.25 is hour. repetition = 0.25*4 = 1 round
### hence, we only need to download these deeplink for once, we need 0.25*4 = 1
#DeepLink(deeplink_list, deeplink_folder,file_names).folder_setup()




#==============================================================================
# Step 4. Parsing deeplinks
#==============================================================================
folder = 'coin_500deeplink'
ParsingDeepLink(folder).parsing_coin_deeplink()
folder = 'gecko_500deeplink'
ParsingDeepLink(folder).parsing_gecko_deeplink()




#==============================================================================
# Step 5. Pair rating urls and names, scrapping rating deeplink
#==============================================================================
rating_url_list, rating_name_list = merge_rating_links()
folder = ['coin_rating_html', 'gecko_rating_html']
DeepLink(rating_url_list, folder, rating_name_list, mode = 0).folder_setup()
os.rmdir(os.path.join(os.getcwd(), 'gecko_rating_html'))




#==============================================================================
# Step 10. Recovering missing data
#==============================================================================
# re-download data from Error_Log.csv






