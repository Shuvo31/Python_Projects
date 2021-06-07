import requests

from bs4 import BeautifulSoup

search="Weather in Kolkata"

url=f"https://www.google.com/webhp{search}"

r =requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
update = s.find("div",class_="BNeawe").text
print(update)