import requests
from bs4 import BeautifulSoup
import lxml

url="https://www.instagram.com/{}"

def scrape(username):
    full_url=url.format(username)
    r=requests.get(full_url)
    s=BeautifulSoup(r.text,"lxml")

    tag=s.find("meta",attrs={'name':'description'})
    text=tag.attrs['content']
    main_text=text.split('-')[0]

    return main_text


username=input("Enter username: ")
data=scrape(username)
print(data)