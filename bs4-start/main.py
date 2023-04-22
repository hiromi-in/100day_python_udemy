from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
#print(response.text)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
#print(soup.title)

#titles = soup.select(selector="table .titleline a")
#print(titles)

article_text = [text.getText() for text in soup.select(selector="table .title .titleline a") if 'http' in text.get("href")]
print(article_text)
article_link = [link.get("href") for link in soup.select(selector="table .titleline a") if 'http' in link.get("href")]
print(article_link)
article_upvote = [int(text.text.split()[0]) for text in soup.select(selector="table .subline .score")]
print(article_upvote)
#print(len(article_upvote))
#print(len(article_link))
#print(len(article_text))

max_index = article_upvote.index(max(article_upvote))
max_title = article_text[max_index]
max_link = article_link[max_index]
max_upvote = article_upvote[max_index]
print(max_title)
print(max_link)
print(max_upvote)





#with open("website.html", encoding = 'cp932', errors='ignore') as file:
#    script = file.read()
#
#soup = BeautifulSoup(script, 'html.parser')
##print(soup.title.string)
##print(soup.prettify())
#
##all_anchor_tags = soup.find_all(name="a")
##print(all_anchor_tags)
#
##for tag in all_anchor_tags:
#   # print(tag.getText())
# #   print(tag.get("href"))
#
#heading = soup.find(name="h1", id="name")
#print(heading)
#
#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.getText())
#print(section_heading.get("class"))
#print(section_heading.name)
#
#company_url = soup.select_one(selector="p a")
#print(company_url)
#
#name = soup.select_one(selector="#name")
#print(name)
#
#headings = soup.select_one(selector=".heading")
#print(headings)