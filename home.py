from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

data = requests.get(url) 

movieFile = open('movies.py', 'w')
all_titles = []
html = BeautifulSoup(data.text, 'html.parser')
mTitles = html.select('table.chart td.titleColumn')
for titles in mTitles:
    titles_text = titles.a.text
    titles_release_date = titles.span.text
    all_titles.append({"Movie Title": titles_text, "Release Date": titles_release_date})    
    movieFile.write(titles_text)
    movieFile.write(titles_release_date)
    print(all_titles)