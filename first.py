import os
import time
import re
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


linklist1 = []
linklist2 = []
linklist3 = []

os.mkdir(r"C:\Newdir")

def getlinks1(url):
    linklist = []
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    for i in bsobj.findAll("div", {"class" : "previews"}):
       for j in i.findAll("a"):
           if 'href' in j.attrs:
               linklist.append("https://worldcosplay.net"+j.attrs['href'])
    return linklist

def getlinks2(url):
    linklist = []
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    for i in bsobj.findAll("div", {"pagemark":"1"}):
        for j in i.findAll("a"):
            if "href" in j.attrs:
                linklist.append("https://worldcosplay.net"+j.attrs["href"])
    return linklist

def get_picture_url(url):
    urls = []
    html = urlopen("url")
    bsobj = BeautifulSoup(html)
    for i in bsobj.findAll("div", {"id":"photoPage"}):
        for j in i.findAll("div", {"id":"photoContainer"}):
            for k in j.findAll("img"):
                if "src" in k.attrs:
                    urls.append(k.attrs["src"])

    return urls

def mkdir(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    name = bsobj.findAll("div", {"class":"selected_character"})
    name = str(name)
    pattern = "(\[)|(\])|(</?\w+[^>]*>)|(\")|(/)"
    name = re.sub(pattern, '', name)
    try:
        os.mkdir("C:\\Newdir\\"+name)
    except FileExistsError:
        path = "C:\\Newdir\\"+name
    path = "C:\\Newdir\\"+name
    return path


url = "https://worldcosplay.net/member/Itsuki-chan/characters"

linklist1 = getlinks1(url)
for i in linklist1:
    linklist2 = getlinks2(i)
    path = mkdir(i)
    for j in linklist2:
        key = j.replace("https://worldcosplay.net/photo/", "")
        path = path + "\\" + key + ".jpg"
        linklist3 = get_picture_url(j)
        for k in linklist3:
            urlretrieve(k, path)
            time.sleep(2)
