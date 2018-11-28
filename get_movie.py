import urllib.request as u
from requests import get
from lxml import html
from bs4 import BeautifulSoup

#Get server response html
#amc = get('https://www.movietickets.com/theaters/detail/id/ti-44118/name/amc-champaign-13')
keys = {'key1': '61801'}
fandango = u.urlopen('https://www.fandango.com/61801_movietimes?mode=general&q=61801')
mybytes = fandango.read()
mystr = mybytes.decode("utf8")
fandango.close()

soup = BeautifulSoup(mystr, "html.parser")


soup = BeautifulSoup(amc.content, "html.parser")
movie_containers = soup.find_all("div", class_ = "small-12 column theater-detail-movie-darken")

movie_names = []
movie_times = []
for movie_container in movie_containers1:
    movie_names.append(movie_container.h4.text)
    movie_times.append(movie_container.find_all('a', class_ = 'button showtime mtc-showtimes'))

for movie_container in movie_containers1:
    showtime_Tags = movie_container.find_all("div", {"class": "showtime-indent"})
    for indent in showtime_Tags:
        buttons = indent.find_all("a", {"class": "button showtime mtc-showtimes"})
        for element in buttons:
            print(element.text)









movie1 = {}
for movie_container in movie_containers:
    movie1.append(movie_container.div.h3.text)






soup2 = BeautifulSoup(gqt.content, "html.parser")
movie_containers2 = soup2.find_all("li", class_ = "gridRow filmItem")
movie2 = []
for movie_container in movie_containers:
    movie2.append(movie_container.h2.text)

print(type(movie_containers))
print(len(movie_containers))
