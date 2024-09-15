import requests, json


data = {"traderUid":"b0b64e7587b63152ac93","pageNo":2,"pageSize":10,"languageType":0}
url = 'https://www.bitget.com/v1/trigger/trace/order/historyList'


headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

headers = {
"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
"apptheme": "dark",
"content-length": "78",
"content-type": "application/json;charset=UTF-8",
"cookie": '_ga=GA1.1.379566937.1698108038; _dx_kvani5r=dcbdc6140de5501d1d534b503e929e51807486efb4182c40740ad54b2a4fe261d13905e0; _ym_uid=1698108040727986268; _ym_d=1698108040; afUserId=83f85ed0-83fd-4438-b6ab-b40690c15b71-p; captcha_v4_user=62f9cb8de0f94e3ea547020ce9931214; _ga_clientid=379566937.1698108038; g_state={"i_l":1,"i_p":1701420033516}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225922959043%22%2C%22first_id%22%3A%22w-892622523-1678325398886-256840120%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiNWYyMDYxYjgxM2MyLTBlMDBiM2NjMDcwNWY4OC0xNzQ2MmM2Yy0yMDczNjAwLTE4YjVmMjA2MWI5YmIyIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiNTkyMjk1OTA0MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%225922959043%22%7D%2C%22%24device_id%22%3A%2218b5f2061b813c2-0e00b3cc0705f88-17462c6c-2073600-18b5f2061b9bb2%22%7D; BITGET_LOCAL_COOKIE={%22bitget_lang%22:%22en%22%2C%22bitget_unit%22:%22USD%22%2C%22bitget_showasset%22:true%2C%22bitget_theme%22:%22black%22%2C%22bitget_valuationunit%22:1%2C%22bitget_layout%22:%22right%22%2C%22bitgt_login%22:false}; bt_sessonid=; bt_newsessionid=; AF_SYNC=1702264216590; _cfuvid=2D_frv4VzzEE_5Z4DmsXNfIKBqBIKTI34SVcEIKrc6w-1702315504329-0-604800000; _ym_isad=2; __cf_bm=8JwiEPFuLq1piSxKj0fpeg4CjPP8cmjKN5rTOcia3xY-1702657585-1-ARCS3FCP8nmo8T6Pte8ScjqNOTHBk16qQ4rnls5+gwZnMfc5Ltd6MC8bbQZnYR3H8IcXOCW6jU2M0GsyPgy6PvM=; _ym_visorc=b; _ga_sessionid=1702657586; bt_rtoken=; dy_token=657c7ffc176YtONQVtnNImUqW8p4OhAxi7Tcilr1; _ga_Z8Q93KHR0F=GS1.1.1702657586.37.1.1702658198.60.0.0',
"devicelanguage": "en_US",
"gaclientid": "379566937.1698108038",
"gaid": "GA1.1.379566937.1698108038",
"gasessionid": "1702657586",
"language": "en_US",
"locale": "en_US",
"origin": "https://www.bitget.com",
"referer": "https://www.bitget.com/copytrading/trader/b0b64e7587b63152ac93/futures",
"sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Linux",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"securitynew": "true",
"terminalcode": "1df84caaadce4b96d0d85c8e24093e1d",
"terminaltype": "1",
"usenewpwdversion": "true",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

r = requests.post(url, headers = headers, data = data)
print(r.status_code)






