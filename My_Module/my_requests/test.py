from my_module import my_requests
# import my_requests

"""-------------------------------------------debug-----------------------------------------------"""
# #single page no sleep(checked)
# url =  'http://www.baidu.com'
# my_requests.auto_requests('baidu_single',url,file_type='.json')
#
# #single page with sleep(checked)
# url =  'http://www.baidu.com'
# my_requests.auto_requests('baidu_single',url,sleep = 2,single_folder=False)
#
# #multi-page no sleep(checked)
# url = 'http://coinmarketcap.com/'
# my_requests.auto_requests('coin_test',url,start_page=1,end_page=2)
#
# #multi-page with sleep(checked)
url = 'http://coinmarketcap.com/'
my_requests.auto_requests('coin_test',url,start_page=3,end_page=4,sleep = 2,single_folder = True)
#
# #ajax single page no sleep(checked)
# url = 'https://tieba.baidu.com/f?kw=cs&ie=utf-8&pn=50'
# my_requests.auto_requests('tieba_test',url,asyn=True)
#
# #ajax single page with sleep(checked)
# url = 'https://tieba.baidu.com/f?kw=cs&ie=utf-8&pn=50'
# my_requests.auto_requests('tieba_test',url,asyn=True,sleep = 2)
#
# #ajax multi-page no sleep(checked)
# url = 'https://tieba.baidu.com/f?kw=cs&ie=utf-8&pn='
# x = ((i-1) * 50 for i in range(1,3))
# my_requests.auto_requests('tieba_test',url,asyn=True,start_page=1,end_page=2,url_numbers = x,single_folder = False)
#
# #ajax multi-page with sleep(checked)
# url = 'https://tieba.baidu.com/f?kw=cs&ie=utf-8&pn='
# x = ((i-1) * 50 for i in range(3,5))
# my_requests.auto_requests('tieba_test',url,asyn=True,normal_page_number = False,start_page=3,end_page=4,url_numbers = x,sleep = 2,single_folder = False)

"""-------------------------------------------debug-----------------------------------------------"""






# url ='https://tieba.baidu.com/f?kw=cs&ie=utf-8&pn='
# x = ((i-1) * 50 for i in range(1,4))
#
# my_requests.auto_requests('test_v1.1',url,start_page=1,end_page=3,normal_page_number = False,url_numbers = x,sleep = 2)
#


# def saving_maker (file_root,file_content,file_type,input_type='w',file_encoding = 'utf-8'):
#     f = open(file_root + file_type + '.tmp',input_type,encoding = file_encoding)
#     f.write(file_content)
#     f.close()
#     os.rename(file_root + file_type + '.tmp',file_root + file_type)






# url = 'https://coinmarketcap.com/'
# my_requests.auto_requests('coin',url,start_page=1,end_page=4,sleep = 10)

"""success!"""
# url_number = (i+1 for i in range(1,4))
# url_numbers = [1,2,3,4]
# if type(url_number) is list:
#     print('method 1')
# elif str(type(url_number)) == "<class 'generator'>":
#     print('yes')
# else:
#     print("'url_numbers' must be a list or generator type")
""""""
# front_url = 'http://coinmarketcap.com/'
# start_page = 1
# end_page = 3
# gen = (i+1 for i in range(1,4))
# url_numbers = []
# while True:
#     if not os.path.exists('folder_name/gen.txt'):
#         f = open('folder_name/gen.txt','w',encoding='utf-8')
#         f.write('release gen')
#         f.close()
#         for x in range(start_page,end_page+1):
#             x = gen.__next__()
#             url_numbers.append(x)
#
#         print(url_numbers)
#     else:
#         for page in url_numbers:
#             full_url = front_url + str(page)
#             print(full_url)
#     time.sleep(2)



# folder_name = 'try_v1.1'
# if not os.path.exists(folder_name +'/'+'gen.py'):
#     os.mkdir(folder_name)
#     f = open(folder_name +'/'+ 'gen.txt', 'w', encoding='utf-8')
#     f.write('release gen')
#     f.close()