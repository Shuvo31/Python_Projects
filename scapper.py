import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.amazon.in/")
soup=BeautifulSoup(req.content,"html.parser")
print(soup.get_text())
print(soup.pretiffy())
