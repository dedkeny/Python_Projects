import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


htmlData = getdata("https://something.com")

soup = BeautifulSoup(htmlData, 'html.parser')
