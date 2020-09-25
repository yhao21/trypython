import re
import glob


for one_file in glob.glob("Coin_Market_Cap_Program/coin_exchange_html_file/exchange_by_volumepage # 1 2020-02-05-12-06-05.html"):
    f = open(one_file,"r",encoding="utf-8")
    content = f.read()
    trs = re.compile(r'<tr class="cmc-table-row" style="display:table-row">(.*?)<tr').findall(content)
    names = re.compile(r'<a href="/exchanges/\w+/" title="\w+" class="cmc-link">(.*?)</a></div>').findall(str(trs))
    adj_Vol_24s = re.compile(r'24-h-adjusted.*?<a href="/exchanges/\w+/#markets" class="cmc-link">(.*?)</a></div>').findall(str(trs))
    volume_24s = re.compile(r'volume-24-h.*?<a href="/exchanges/\w+/#markets" class="cmc-link">(.*?)</a></div>.*volume-7-d').findall(str(trs))
    volume_7days = re.compile(r'volume-7-d.*?<a href="/exchanges/\w+/#markets" class="cmc-link">(.*?)</a></div>.*?volume-30-d').findall(str(trs))
    print(len(adj_Vol_24s))
    # for i in range(1,len(names)):
    #     name = names[i]
        # print (name)
