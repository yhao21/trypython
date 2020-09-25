
Date:	03/26/2020
Auther: Yan





INSTRUCTIONS:



NOTICE:

    Please [MAKE SURE] you have downloaded [ALL] the coding files, and put them in the [SAME] folder! There are 7 python files and 1 text file.
	Check List:
		1. start_scrapping.py
		2. web_scrapping.py
		3. parsing_each_day_link.py
		4. scrapping_each_day.py
		5. parsing_each_day.py
		6. scrapping_each_movie.py
		7. parsing_each_movie.py
		8. README.txt
    Packages you need to have: Pandas, Numpy, Requests, BeautifulSoup, Os, Glob, Time, Re.
    The full version will cost you a lot of time to download and parse the pages, you may want to use [ TEST VERSION ] if you need a quick feedback.


------------------------------------------------------------------Auto-Working Instructions------------------------------------------------------------------------------------------------------------------------

If you want this program work automatically, the ONLY thing you need to do is: Open [ start_scrapping.py ], and change 'year_list' to the year(s) you want.
    The default value of 'year_list' is years from 2014 to 2020. If you want to change it, make sure 'year_list' is in LIST form.

    The program will AUTOMATICALLY do the following steps
    Step 1: The program will download each year's information to a new folder [ box_office_pages ], files are named by year.
    Step 2: The program will parse files for each year, and save each date's url to [ date_links.csv ] under root path.
    Step 3: The program will scrapping all the movies in each day, and save html files to a new folder [ Each_Day_Info ]. Html files are named by dates.
    Step 4: The program will parse files for each day, and save information to [ every_day_movies.csv ]. It will save the link of each movie to a separate file [ movie_links.csv ].
    Step 5: The program will scrapping each movie's webpage, and save html files to folder [ Each_Movie_Info ]. Html files are named by dates and the movie names.
    Step 6: The program will parse files for each movie, and save information to [ movie_detail_info.csv ].
    Step 7: The program will merge [ movie_detail_info.csv ] and [ every_day_movies.csv ] to [ Box Office Info Merge.csv ]. You can check all the required info in this csv file.



------------------------------------------------------------------Manual Check Instructions------------------------------------------------------------------------------------------------------------------------



Part I: Scrapping year-data

    Object file: web_scrapping.py

    You can run this file directly, or import it as a module.
    If you choose to run it directly, modify the 'year list' under [ if __name__ == "__main__": ]
    The initial 'year_list' is from 2014 to 2020
        Example:
            if __name__ == "__main__":
                year_list = [2013,2018,2020]
                web_scrapping(year_list)

    If you choose to import it as a module, 'year_list' is the only parameter you need to submit.
        Example:
            import web_scrapping

            year_list = [1990,1993,2001,2020]
            web_scrapping.web_scrapping(year_list)

    Notice:
        1. This website currently only provides data in year 1977, 1980, 1982 ~ 2020.
           If your 'year list' contains year(s) other than these, this program will send you an error report.
        2. 'year_list' must be a list.




Part II: Parsing each day's link

    Object file: parsing_each_day_link.py

    You can run this file directly, or import it as a module.
    It will gather the link for each day, and save them to "date_links.csv".

    If you choose to import it as a module, you do not need to send any parameter into the function.
        Example:
            import parsing_each_day_link

            parsing_each_day_link.parsing_each_day_link()



Part III: Get each day's info

    Section I: Scrapping each day's page

        Object file: scrapping_each_day.py

        You can run this file directly, or import it as a module.
        It will download daily webpage to a folder, named Each_Day_Info. Each html file is named as the date it is.

        If you choose to import it as a module, you do not need to send any parameter into the function.
            Example:
                import scrapping_each_day

                scrapping_each_day.scrapping_each_day()

    Section II: Parsing each day's page

        Object file: parsing_each_day.py

        You can run this file directly, or import it as a module.
        It will parse each day's html file, gather information ['movie name','daily box office','theaters',
        'gross box office to date','number of days in release','distributer'], and save them to "every_day_movies.csv".
        Also, it will save each movies url to "movie_links.csv" for Part IV.

        If you choose to import it as a module, you do not need to send any parameter into the function.
            Example:
                import parsing_each_day

                parsing_each_day.parsing_each_day()


Part IV: Get each movie's info

    Section I: Scrapping each movie page

    Object file: scrapping_each_movie.py

    You can run this file directly, or import it as a module.
    It will download each movie's webpage to a folder, named Each_Movie_Info. Each html file is named as a combination of date and movie name.

    If you choose to import it as a module, you do not need to send any parameter into the function.
        Example:
            import scrapping_each_movie

            scrapping_each_movie.scrapping_each_movie()

    Section II: Parsing each movie page

    Object file: parsing_each_movie.py

    You can run this file directly, or import it as a module.
    It will parse each movie's html file, andgather information ['Movie Name','Opening Money',
    'Release Date','MPAA','Running Time','Genre','In Release Period','Widest Release','ID of IMDbPro'],
    and save them to "movie_detail_info.csv".

    If you choose to import it as a module, you do not need to send any parameter into the function.
        Example:
            import parsing_each_movie

            parsing_each_movie.parsing_each_movie()





