import requests
from bs4 import BeautifulSoup


r=requests.get("https://www.nytimes.com/")
soup=BeautifulSoup(r.text,"html.parser")
title=soup.find("title")
print(title)