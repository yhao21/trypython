import glob
import re
import pandas as pd

df = pd.DataFrame()



for one_file in glob.glob("tieba_pubg_html_file/pages/*.html"):
    f = open(one_file, "r",encoding="utf-8")
    """
    注意：f.read一定要事先赋值给一个变量，不能放到findall里面，f.read只能执行一次，这就是为什么如果放在findall当中，其中一个df为空
    """
    content = f.read()
    try:
        names = re.compile(r'<a rel="noreferrer" .* class="j_th_tit ">(.*)</a>.*').findall(content)
        authors = re.compile(r'title="主题作者:(.*?)" data-field').findall(content)
        for i in range(len(names)+1):
            name = names[i]
            author = authors[i]
            df = df.append({
                "name":name,
                "author": author
            },ignore_index=True)
    except:
        pass


print(df)
