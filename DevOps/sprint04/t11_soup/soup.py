from bs4 import BeautifulSoup, SoupStrainer
import requests as req
import sys
import re
import json


page = req.get(sys.argv[1])
soup = BeautifulSoup(page.text,"html.parser")
name_bdf = soup.title.string.strip().split(' — ')[0].replace(' ','_')
name_json = re.sub("[^0-9a-zA-Z\s_]+", "", name_bdf) + ".json"
mydivs = soup.find_all("a",class_="reference external")
final_list = []
for i in mydivs:
    part_json = {}
    pages = req.get(i["href"])
    titles = None
    soups = BeautifulSoup(pages.text,"html.parser")
    try:
        titles = soups.title.string
    except:
        pass
    part_json.update({"link_text" : i.text, "url" : i["href"],\
        "title" : titles})
    final_list.append(part_json)
with open(name_json, 'w') as outfile:
    json.dump(final_list, outfile, indent=1)