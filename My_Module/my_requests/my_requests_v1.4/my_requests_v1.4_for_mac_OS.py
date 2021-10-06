import os,requests,time
from selenium import webdriver



def folder_tree(folder_name,ini_count,single_folder):
    current_time = time.strftime(' Time  %Y.%m. %d %H_%M_%S')
    sub_folder_name = str(ini_count) + '. ' + str(current_time)
    if single_folder is True:
        root =  folder_name + '/'
        file_name = root + 'page # '
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

    elif single_folder is False:
        root = folder_name + '/' + sub_folder_name + '/'
        file_name = root + 'page # '
        if not os.path.exists(folder_name + '/' + sub_folder_name):
            os.mkdir(folder_name + '/' + sub_folder_name)
    else:
        print('Error: invalid args value for single_folder!')


    return file_name#root

def sel_way(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html


def requests_way(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    html = r.text
    return html


def file_making(file_root,file_type,file_content,write_way='w',file_encoding='utf-8'):
    f = open(file_root + file_type + '.temp',write_way,encoding = file_encoding)
    f.write(file_content)
    f.close()
    os.rename(file_root + file_type + '.temp',file_root + file_type)


def page_download(folder_name,front_url,start_page,end_page,normal_page_number,url_numbers,url_rear,nap,sleep,ini_count,arith_url_numbers,ways,single_folder,file_type):
    tree = folder_tree(folder_name,ini_count,single_folder)
    if start_page == '' and end_page == '':
        if single_folder is True:
            file_time = time.strftime(' Time  %Y.%m. %d %H_%M_%S')
            if os.path.exists(tree + file_time + file_type):
                print(tree + file_time + file_type + ' is existed')
            else:
                url = front_url
                web_con = ways(url)
                file_making(tree + file_time,file_type,web_con)
                print("Finish downloading html file! " + file_time)
                time.sleep(nap)

        elif single_folder is False:
            url = front_url
            web_con = ways(url)
            file_making(tree, file_type, web_con)
            print("Finish downloading html file!")
            time.sleep(nap)

    else:
        if normal_page_number ==True:
            for page_number in range(start_page,end_page+1):
                if single_folder is True:
                    if os.path.exists(tree + str(page_number) + file_type):
                        print(tree + str(page_number) + file_type + ' is existed')
                    else:
                        url = front_url + str(page_number) +url_rear
                        web_con = ways(url)
                        file_making(tree + str(page_number),file_type,web_con)
                        print('Finish downloading page # ' + str(page_number) + '......')
                        time.sleep(nap)

                elif single_folder is False:
                    url = front_url + str(page_number) + url_rear
                    web_con = ways(url)
                    file_making(tree + str(page_number), file_type, web_con)
                    print('Finish downloading page # ' + str(page_number) + '......')
                    time.sleep(nap)

        else:
            if type(url_numbers) is list:
                for page_number in url_numbers:
                    if single_folder is True:
                        if os.path.exists(tree + str(page_number) + file_type):
                            print(tree + str(page_number) + file_type + ' is existed')
                        else:
                            url = front_url + str(page_number) + url_rear
                            web_con = ways(url)
                            file_making(tree + str(page_number),file_type,web_con)
                            print('Finish downloading page # ' + str(page_number) + '......')
                            time.sleep(nap)
                    elif single_folder is False:
                        url = front_url + str(page_number) + url_rear
                        web_con = ways(url)
                        file_making(tree + str(page_number), file_type, web_con)
                        print('Finish downloading page # ' + str(page_number) + '......')
                        time.sleep(nap)

            elif str(type(url_numbers)) == "<class 'generator'>":
                for arith_number in arith_url_numbers:
                    if single_folder is True:
                        if os.path.exists(tree + str(arith_number) + file_type):
                            print(tree + str(arith_number) + file_type + ' is existed')
                        else:
                            url = front_url + str(arith_number) + url_rear
                            web_con = ways(url)
                            file_making(tree + str(arith_number),file_type,web_con)
                            print('Finish downloading page # ' + str(arith_number) + '......')
                            time.sleep(nap)
                    elif single_folder is False:
                        url = front_url + str(arith_number) + url_rear
                        web_con = ways(url)
                        file_making(tree + str(arith_number), file_type, web_con)
                        print('Finish downloading page # ' + str(arith_number) + '......')
                        time.sleep(nap)

            else:
                print("Error! 'url_numbers' must be a list or generator type.")

    time.sleep(sleep)



def auto_requests(folder_name,url,asyn=False,start_page = '',end_page = '',normal_page_number = True,url_numbers='',url_rear = '/',nap = 0,sleep = 0,ini_count = 0,single_folder = True,file_type = '.html'):

    front_url = url
    arith_url_numbers = []

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    if str(type(url_numbers)) == "<class 'generator'>":
        for x in range(start_page, end_page + 1):
            x = url_numbers.__next__()
            arith_url_numbers.append(x)

    if asyn is False:
        ways = requests_way

    elif asyn is True:
        ways = sel_way

    if sleep == 0:
        page_download(folder_name, front_url, start_page, end_page, normal_page_number, url_numbers, url_rear, nap, sleep,ini_count, arith_url_numbers, ways,single_folder,file_type)
    elif sleep != 0:
        while True:
            print('\nStart downloading Round # ' + str(ini_count) + '\n')
            page_download(folder_name,front_url,start_page,end_page,normal_page_number,url_numbers,url_rear,nap,sleep,ini_count,arith_url_numbers,ways,single_folder,file_type)
            ini_count += 1










