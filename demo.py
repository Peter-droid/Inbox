
##########################
##########################
    import os
    from urllib.request import urlretrieve
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import time
##########################
linklist = []
for i in bsobj.findAll("div", {"class" : "previews"}):
   for j in i.findAll("a"):
       if 'href' in j.attrs:
           linklist.append(j.attrs['href'])
##########################
    def getlinks2(url):
    linklist = []
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    for i in bsobj.findAll("li", {"class":"ng-scope"}):
        for j in i.findAll("a"):
            if "href" in j.attrs:
                linklist.append("https://worldcosplay.net"+j.attrs["href"])
    return linklist
##########################
def get_picture_url(url):
    urls = []
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    for i in bsobj.findAll("div", {"id":"phtotPage"}):
        for j in i.findAll("img"):
            if "src" in j.attrs:
                urls.append(j.attrs["src"])
    return urls
##########################
    def create_path():
    path =

    return path
##########################
def download(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    name = bsobj.findAll("h1", {"itemprop":"name"})
    os.mkdir(r"C:\Newdir"+name)
    urlretrieve(url, r"C:\Newdir"+name)

html = urlopen(url)
bsobj = BeautifulSoup(html)
name = bsobj.findAll("div", {"class":"selected_character"})

#def getlinks2(url):
    linklist = []
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    for i in bsobj.findAll("div", {"pagemark":"1"}):
        for j in i.findAll("a"):
            if "href" in j.attrs:
                linklist.append("https://worldcosplay.net"+j.attrs["href"])
    return linklist

def getlinks2(url):
    for i in range(1, 4):
        i = str(i)
        url = url.replace("/member/Itsuki-chan/characters/", "/api/member/126641/characters/")
        url_new = url + "photos.json?limit=16&p3_photo_list=true&page=" + i
        html = urlopen(url_new)
        bsobj = BeautifulSoup(html)
        text1 = bsobj.text.replace("false", "\'false\'")
        text2 = text1.replace("true", "\'true\'")
        text3 = text2.replace("null", "\'null\'")
        pattern = "0-9"
        text4 = re.sub(re.compile(pattern),'', text3)
        index = eval(text4)
        for i in index["list"]:
            dic = i["photo"]
            linklist2.append("https://worldcosplay.net"+dic["url"])
