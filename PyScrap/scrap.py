
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

html = urlopen("https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC")

try:
    
    bsObj = BeautifulSoup(html.read(), "html.parser")

    imgs = bsObj.findAll("img")
    for img in imgs:
        print(img)
        

except HTTPError as e:
    print(e)


