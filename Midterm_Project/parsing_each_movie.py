import pandas as pd
import os,glob,re





def parsing_each_movie():

    assert str(os.listdir('Each_Movie_Info')) != '[]', \
        "You should download each day's page first!\n\nCheck if you have run [ scrapping_each_movie.py ]"

    movie_info = pd.DataFrame()
    for one_file in glob.glob('Each_Movie_Info/*.html'):
        f = open(one_file,'r',encoding = 'utf-8')
        html = f.read()
        opening_money = str(re.compile(r'Opening.*<span class="money">(.*?)</span>').findall(html)).replace("['",'').replace("']",'').replace('$','')
        release_date1 = str(re.compile(r'Release Date</span><.*bo_rl_rl">(.*?)</a').findall(html)).replace("['",'').replace("']",'')
        release_date2 = str(re.compile(r'ref_=bo_rl_rl">(.*?)</a></span></div><d').findall(html)).replace("['",'').replace("']",'')
        release_date = release_date1 + ' - ' + release_date2
        mpaa = str(re.compile(r'MPAA</span><span>(.*?)</span>').findall(html)).replace("['",'').replace("']",'')
        run_time_pre = str(re.compile(r'Running Time</span><span>(.*?)<').findall(html)).replace("['",'').replace("']",'')
        hours = int(re.compile(r'\d').search(run_time_pre).group())
        mins_pre = int(re.compile(r'hr (\d+)').search(run_time_pre).group().replace('hr ',''))/60
        mins = mins_pre.__round__(2)
        run_time_dig = hours + mins
        run_time = run_time_dig.__round__(2)
        genre = str(re.compile(r'Genres</span><span>(\w*.*?)</span></div>',re.S).findall(html)).replace("['",'').replace("']",'').replace('\\n','').replace(r'            ',' ')
        in_release_period = str(re.compile(r'In Release</span><span>(\d*) days/').findall(html)).replace("['",'').replace("']",'')
        widest_release = str(re.compile(r'Widest Release</span><span>(.*?) theaters</span>').findall(html)).replace("['",'').replace("']",'')
        IMDbPro = str(re.compile(r'href="https://pro.imdb.com/title/(.*?)/cast.*ref_=mojo_rl_summary&amp;rf=mojo_rl_summary',re.S).findall(html)).replace("['",'').replace("']",'')
        name = str(re.compile(r'<h1 class="a-size-extra-large">(.*?)</h1>').findall(html)).replace("['",'').replace("']",'')
        dates = str(re.compile(r'\d{4}-\d{2}-\d{2}').search(one_file).group())
        movie_info = movie_info.append({
            'Date1':dates,
            'Movie Name1': name,
            'Opening Money':opening_money,
            'Release Date':release_date,
            'MPAA':mpaa,
            'Running Time':run_time,
            'Genre':genre,
            'In Release Period':in_release_period,
            'Widest Release':widest_release,
            'ID of IMDbPro':IMDbPro
        },ignore_index = True)

        order = ['Date1','Movie Name1','Opening Money','Release Date','MPAA','Running Time','Genre','In Release Period','Widest Release','ID of IMDbPro']
        movie_info = movie_info[order]

    print(movie_info)
    movie_info.to_csv('movie_detail_info.csv')




if __name__ == "__main__":

    parsing_each_movie()
