import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
#print(soup.prettify())

find_all = soup.find_all(name="h3", class_="title")
find_all_list = [movie.getText() for movie in find_all]
find_all_list.reverse()
for item in find_all_list:
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{item}\n")


