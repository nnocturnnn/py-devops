from bs4 import BeautifulSoup, SoupStrainer
import re
import requests as req

page = req.get("https://docs.python.org/3/library/unicodedata.html")
print(page.text)
soup = BeautifulSoup(page.text,"html.parser")
mydivs = soup.find_all("a",class_="reference external")
print(len(mydivs))
