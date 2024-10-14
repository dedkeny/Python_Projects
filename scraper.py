import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


url = input("Enter URL: ")

htmlData = getdata(url)

soup = BeautifulSoup(htmlData, 'html.parser')
