import pandas as pd
import os,glob,re,time,math



def left_time_estimation(round_time,remain_workload):
    left_time = remain_workload * round_time
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...(6/6)')
    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(6/6)')
    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(6/6)')
    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(6/6)')



def parsing_each_movie():

    assert str(os.listdir('Each_Movie_Info')) != '[]', \
        "You should download each day's page first!\n\nCheck if you have run [ scrapping_each_movie.py ]"

    movie_info = pd.DataFrame()

    for one_file in glob.glob('Each_Movie_Info/*.html'):

        loads = [file for file in glob.glob('Each_Movie_Info/*.html')]
        position = loads.index(one_file)
        remain_workload = len(loads) - position
        round_s_time = time.time()
        file_name = one_file.replace('Each_Movie_Info\\', '').replace('.html','')


        f = open(one_file,'r',encoding = 'utf-8')
        html = f.read()
        f.close()
        opening_money_pre = str(re.compile(r'Opening.*<span class="money">(.*?)</span>').findall(html))
        if opening_money_pre != '[]':
            opening_money = opening_money_pre.replace("['",'').replace("']",'').replace('$','')
        else:
            opening_money = 'No Information'

        release_date_pre = re.compile(r'bo_rl_rl">([a-zA-Z]{3}.*?)</a').findall(html)
        if len(release_date_pre) == 2:
            release_date1 = release_date_pre[0]
            release_date2 = release_date_pre[1]
            release_date = release_date1 + ' - ' + release_date2
        if len(release_date_pre) == 1:
            release_date = release_date_pre[0]

        mpaa_pre = str(re.compile(r'MPAA</span><span>(.*?)</span>').findall(html))
        if mpaa_pre != '[]':
            mpaa = mpaa_pre.replace("['",'').replace("']",'')
        else:
            mpaa = 'No Information'

        run_time_pre = str(re.compile(r'Running Time</span><span>(.*?)<').findall(html)).replace("['",'').replace("']",'')
        try:
            hours = int(re.compile(r'\d').search(run_time_pre).group())
        except:
            hours = 0
        try:
            mins_pre = int(re.compile(r'hr (\d+)').search(run_time_pre).group().replace('hr ',''))/60
        except:
            mins_pre = 0
        mins = mins_pre.__round__(2)
        run_time_dig = hours + mins
        run_time = run_time_dig.__round__(2)
        genre = str(re.compile(r'Genres</span><span>(\w*.*?)</span></div>',re.S).findall(html)).replace("['",'').replace("']",'').replace('\\n','').replace(r'            ',' ')
        in_release_period = str(re.compile(r'In Release</span><span>(.*?) days/').findall(html)).replace("['",'').replace("']",'')
        widest_release = str(re.compile(r'Widest Release</span><span>(.*?) theater').findall(html)).replace("['",'').replace("']",'')
        IMDbPro = str(re.compile(r'href="https://pro.imdb.com/title/(.*?)/cast.*ref_=mojo_rl_summary&amp;rf=mojo_rl_summary',re.S).findall(html)).replace("['",'').replace("']",'')
        name = file_name
        movie_info = movie_info.append({
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

        order = ['Movie Name1','Opening Money','Release Date','MPAA','Running Time','Genre','In Release Period','Widest Release','ID of IMDbPro']
        movie_info = movie_info[order]

        round_e_time = time.time()
        round_time = round_e_time - round_s_time
        left_time_estimation(round_time, remain_workload=remain_workload)

    print(movie_info)
    movie_info.to_csv('movie_detail_info.csv')




if __name__ == "__main__":

    parsing_each_movie()