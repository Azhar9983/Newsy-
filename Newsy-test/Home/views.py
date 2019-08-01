from django.shortcuts import render
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen as ureq
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#opening urls
def open_page(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = ureq(request)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser", from_encoding="iso-8859-1")
    return page_soup

# Home scrapping functions
def scraptmi():
    page_soup = open_page("https://timesofindia.indiatimes.com/")
    container = page_soup.find("div", {"class": "top-story"})
    news = container.find_all('li')
    key = {}
    for headline in news:
        s = headline.a["href"]
        if s.startswith("/"):
            s="https://timesofindia.indiatimes.com"+s
        key[headline.a.text] = s

    return key.items()

def scraphindu():
    page_soup = open_page("https://www.thehindu.com/")
    container = page_soup.find("div", {"class": "main"})
    data = container.find_all("div", {"class": "story-card-news"})
    key = {}
    for headline in data:
        key[headline.h2.a.text] = headline.h2.a["href"]
    return key.items()

def scrapndtv():
    page_soup = open_page("https://www.ndtv.com/")
    container = page_soup.find("div", {"class": "cont_cmn top-stories-68"})
    news = container.find_all('li')
    key = {}
    for headline in news:
        a = headline.find('a', {"class": "item-title"})
        key[a.text] = a["href"]
        #key.append(a.text + "*&*" + a["href"])
    return key.items()

def scrapindexp():
    page_soup = open_page("https://indianexpress.com/")
    key= {}
    container = page_soup.find_all("div", {"class": "l-grid__item one-half@medium+"})
    for i in range(0, 2):
        news = container[i].find_all('div', {"class": "l-grid__item l-grid__item--divided one-half@small m-read-article"})
        for headline in news:
            key[headline.a["title"]] = headline.a["href"]
    return key.items()

def scrapht():
    page_soup = open_page("https://www.hindustantimes.com/")
    container = page_soup.find("div", {"class": "latestnews-left"})
    data = container.find_all("li")
    key = {}
    for headline in data:
        key[headline.h2.a.text] = headline.h2.a["href"]
    return key.items()

def scraptnews18():
    page_soup = open_page("https://www.news18.com/")
    key = {}
    container = page_soup.find("ul", {"class": "lead-mstory"})
    data = container.find_all("li")
    for headline in data:
        key[headline.a.text] = headline.a["href"]
    return key.items()

#India scrapping functions

def indiatmi():
    page_soup = open_page("https://timesofindia.indiatimes.com/india")
    container = page_soup.find("div", {"class": "main-content"})
    news = container.find("ul", {"class": "top-newslist clearfix"})
    key = {}
    for headline in news:
        s = headline.a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[headline.a["title"]] = s

    news2 = container.find("ul", {"class": "list5 clearfix"})

    for headline2 in news2:
        s = headline2.a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[headline2.a.text] = s
    return key.items()
def indiahindu():
    page_soup = open_page("https://www.thehindu.com/news/national/")
    container = page_soup.find("div", {"class": "justin-100x3-container hidden-xs"})
    # print(container)
    data = container.find_all("ul")
    key = {}
    for ss in data:
        x = ss.find_all("li")
        for z in x:
            s = z.h3.a.text.strip().split("\n")
            try:
                key[s[2]] = z.h3.a["href"]
            except IndexError:
                continue
    return key.items()
def indiaht():
    page_soup = open_page("https://www.hindustantimes.com/india-news/")
    container = page_soup.find("div", {"class": "col-sm-7 col-md-8 col-lg-9"})
    data = container.findAll("li")
    key = {}
    for i in range(0, 11):
        key[data[i].img["alt"]] = data[i].a["href"]
    return key.items()
def indiaindexp():
    page_soup = open_page("https://indianexpress.com/section/india/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.h3.a.text] = head.h3.a["href"]
    return key.items()
def indiandtv():
    page_soup = open_page("https://www.ndtv.com/india?pfrom=home-mainnavgation")
    container = page_soup.find("div", {"class": "new_storylising"})
    data = container.findAll("div", {"class": "nstory_header"})
    key = {}
    for i in range(0, 11):
        key[data[i].a.text.strip()] = data[i].a["href"]
    return key.items()
def indianews18():
    page_soup = open_page("https://www.news18.com/india/?ref=topnav")
    container = page_soup.find("div", {"class": "blog-list"})
    data = container.findAll("div", {"class": "blog-list-blog"})
    key ={}
    for i in range(0, 11):
        key[data[i].a.img["alt"]] = data[i].a["href"]
    return key.items()

#World scrapping functions
def worldtmi():
    page_soup =open_page("https://timesofindia.indiatimes.com/world")
    container = page_soup.find("div", {"class": "top-newslist"})
    data = container.find_all("li")
    key = {}
    for head in data:
        s = head.a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[head.a["title"]] = s
    return key.items()
def worldht():
    page_soup = open_page("https://www.hindustantimes.com/world-news/")
    container = page_soup.find("ul", {"class": "latest-news-morenews more-latest-news more-separate newslist-sec"})
    head = container.find_all("li")
    key = {}
    for i in range(0, 11):
        key[head[i].img["title"]] = head[i].a["href"]
    return key.items()
def worldndtv():
    page_soup = open_page("https://www.ndtv.com/world-news?pfrom=home-mainnavgation")
    container = page_soup.find("div", {"class": "newins_widmid"})
    head = container.find_all("div", {"class": "description"})
    key = {}
    for data in head:
       key[data.a.text] = data.a["href"]
    return key.items()
def worldnews18():
    page_soup = open_page("https://www.news18.com/world/?ref=topnav")
    container = page_soup.find("div", {"class": "hotTopic clearfix"})
    head = container.find_all("li")
    key = {}
    for data in head:
        key[data.a.text] = data.a["href"]
    return key.items()
def worldindexp():
    page_soup = open_page("https://indianexpress.com/section/world/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.a["title"]] = head.a["href"]
    return key.items()
def worldhindu():
    page_soup = open_page("https://www.thehindu.com/news/international/")
    container = page_soup.find_all("div", {"class": "main"})
    content = container[3].find_all("div", {"class": "story-card-news"})
    key = {}
    for head in content:
        key[head.h3.a.text] = head.h3.a["href"]
    return key.items()

#Entertainment scrapping functions
def etmi():
    page_soup = open_page("https://timesofindia.indiatimes.com/etimes")
    container = page_soup.find("div", {"id": "homeatfmovieswidget"})
    content = container.find("ul", {"class": "ent_music_listing"})
    data = content.find_all("li")
    key = {}
    for i in range(0, 12):
        s = data[i].a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[data[i].a["title"]] = s
    return  key.items()
def eht():
    page_soup = open_page("https://www.hindustantimes.com/entertainment/")
    container = page_soup.find("ul", {"class": "latest-news-morenews more-latest-news more-separate newslist-sec"})
    head = container.find_all("li")
    key = {}
    for i in range(0, 11):
        key[head[i].img["title"]] = head[i].a["href"]
    return key.items()
def enews18():
    page_soup = open_page("https://www.news18.com/movies/?ref=topnav")
    container = page_soup.find("div", {"class": "hotTopic clearfix"})
    head = container.find_all("li")
    key = {}
    for data in head:
        key[data.a.text] = data.a["href"]
    return key.items()
def eindexp():
    page_soup = open_page("https://indianexpress.com/section/entertainment/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.a["title"]] = head.a["href"]
    return key.items()
def endtv():
    page_soup = open_page("https://gadgets.ndtv.com/entertainment")
    container = page_soup.find("div", {"class": "nlist bigimglist"})
    data = container.findAll("li")
    key = {}
    for i in range(0, 8):
        key[data[i].a.text] = data[i].a["href"]
    return key.items()
def ehindu():
    page_soup  = open_page("https://www.thehindu.com/entertainment/")
    container =page_soup.find("section",{"id":"section_2"})
    data=container.findAll("p",{"class":"story-card-33-heading"})
    key = {}
    for i in range(0,4):
        key[data[i].a.text] = data[i].a["href"]
    return key.items()

#Life Style scrapping functoins
def lifetmi():
    page_soup = open_page("https://timesofindia.indiatimes.com/etimes")
    container = page_soup.find("div", {"id": "homeatflifewidget"})
    content = container.find("ul", {"class": "ent_music_listing"})
    data = content.find_all("li")
    key = {}
    for i in range(0, 12):
        s = data[i].a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[data[i].a["title"]] = s
    return key.items()
def lifenews18():
    page_soup = open_page("https://www.news18.com/lifestyle/?ref=topnav")
    container = page_soup.find("div", {"class": "hotTopic clearfix"})
    head = container.find_all("li")
    key = {}
    for data in head:
        key[data.a.text] = data.a["href"]
    return key.items()
def lifeindexp():
    page_soup = open_page("https://indianexpress.com/section/lifestyle/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.a["title"]] = head.a["href"]
    return key.items()
def lifeht():
    page_soup = open_page("https://www.hindustantimes.com/lifestyle/")
    container = page_soup.find("ul", {"class": "latest-news-morenews more-latest-news more-separate newslist-sec"})
    head = container.find_all("li")
    key = {}
    for i in range(0, 11):
        key[head[i].img["title"]] = head[i].a["href"]
    return key.items()
def lifehindu():
    page_soup = open_page("https://www.thehindu.com/life-and-style/")
    container = page_soup.find_all("div", {"class": "main"})
    content = container[8].find_all("div", {"class": "story-card-news"})
    key = {}
    for head in content:
        key[head.h3.a.text] = head.h3.a["href"]
    return key.items()
def lifendtv():
    page_soup = open_page("https://swirlster.ndtv.com/?pfrom=home-header-globalnav")
    container = page_soup.find("div", {"class": "row galcont videoscont"})
    data = container.findAll("li")
    key = {}
    for i in range(0, 8):
        key[data[i].h3.a.text] = data[i].a["href"]
    return key.items()

#Sports scrapping functions
def sportstmi():
    page_soup = open_page("https://timesofindia.indiatimes.com/sports")
    container = page_soup.find("div", {"class": "main-content span-8"})
    news = container.find("ul", {"class": "cvs_wdt clearfix"})
    head = news.find_all("li")
    key = {}
    for headline in head:
        s = headline.a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[headline.a["title"]] = s
    return key.items()
def sportnews18():
    page_soup = open_page("https://www.news18.com/sports/?ref=topnav")
    container = page_soup.find("div", {"class": "hotTopic clearfix"})
    head = container.find_all("li")
    key = {}
    for data in head:
        key[data.a.text] = data.a["href"]
    return key.items
def sportsindexp():
    page_soup = open_page("https://indianexpress.com/section/sports/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.a["title"]] = head.a["href"]
    return key.items()
def sportsht():
    page_soup = open_page("https://www.hindustantimes.com/sports-news/")
    container = page_soup.find("ul", {"class": "latest-news-morenews more-latest-news more-separate newslist-sec"})
    head = container.find_all("li")
    key = {}
    for i in range(0, 11):
        key[head[i].img["title"]] = head[i].a["href"]
    return key.items()
def sportshindu():
    page_soup = open_page("https://www.thehindu.com/sport/")
    container = page_soup.find("div", {"class": "wrapXpromo"})
    data = container.findAll("div", {"class": "crossPromo"})
    key = {}
    for i in range(0, 6):
        key[data[i].h3.text] = data[i].a["href"]
    return key.items()
def sportsndtv():
    page_soup = open_page("https://sports.ndtv.com/")
    container = page_soup.find("div", {"class": "mod mod-story-listing"})
    news = container.find_all("div", {"class": "post-content"})
    key = {}
    for headline in news:
        key[headline.h3.a.text] = headline.h3.a["href"]
    return key.items()

#Business scrapping functions
def buisnesstmi():
    page_soup = open_page("https://timesofindia.indiatimes.com/business")
    container = page_soup.find("div", {"class": "top-newslist"})
    data = container.find_all("li")
    key = {}
    for head in data:
        s = head.a["href"]
        if s.startswith("/"):
            s = "https://timesofindia.indiatimes.com" + s
        key[head.a["title"]] = s
    return key.items()
def businessnews18():
    page_soup = open_page("https://www.news18.com/business/?ref=topnav")
    container = page_soup.find("div", {"class": "hotTopic clearfix"})
    head = container.find_all("li")
    key = {}
    for data in head:
        key[data.a.text] = data.a["href"]
    return key.items
def businessindexp():
    page_soup = open_page("https://indianexpress.com/section/business/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.a["title"]] = head.a["href"]
    return key.items()
def businessndtv():
    page_soup = open_page("https://www.ndtv.com/business?pfrom=home-footer")
    container = page_soup.find("div", {"class": "bud_otherstories1"})
    data = container.findAll("p", {"class": "headline"})
    key = {}
    for head in data:
        key[head.a.text] = head.a["href"]
    return key.items()
def businessht():
    page_soup = open_page("https://www.hindustantimes.com/business-news/")
    container = page_soup.find("ul", {"class": "latest-news-morenews more-latest-news more-separate newslist-sec"})
    head = container.find_all("li")
    key = {}
    for i in range(0, 11):
        key[head[i].img["title"]] = head[i].a["href"]
    return key.items()
def businesshindu():
    page_soup = open_page("https://www.thehindu.com/business/")
    container = page_soup.find_all("div", {"class": "main"})
    content = container[5].find_all("div", {"class": "story-card-news"})
    key = {}
    for head in content:
        key[head.h3.a.text] = head.h3.a["href"]
    return key.items()

#Technology scrapping functions
def technews18():
    page_soup = open_page("https://www.news18.com/tech/?ref=topnav")
    container = page_soup.find("div", {"class": "hotTopic clearfix"})
    head = container.find_all("li")
    key = {}
    for data in head:
        key[data.a.text] = data.a["href"]
    return key.items
def techindexp():
    page_soup = open_page("https://indianexpress.com/section/technology/")
    container = page_soup.find("div", {"class": "a-pt5"})
    data = container.find_all("div", {"class": "l-grid__item l-grid__item--divided"})
    key = {}
    for head in data:
        key[head.a["title"]] = head.a["href"]
    return key.items()
def techtmi():
    page_soup = open_page("https://www.gadgetsnow.com/?utm_source=toiweb&utm_medium=referral&utm_campaign=toiweb_hptopnav")
    container = page_soup.find("div", {"class": "span4"})
    data = container.find_all("li")
    key = {}
    for head in data:
        s = head.a["href"]
        if s.startswith("/"):
            s = "https://www.gadgetsnow.com" + s
        key[head.a["title"]] = s
    return key.items()
def techht():
    page_soup = open_page("https://www.hindustantimes.com/tech/")
    container = page_soup.find("ul", {"class": "latest-news-morenews more-latest-news more-separate newslist-sec"})
    head = container.find_all("li")
    key = {}
    for i in range(0, 11):
        key[head[i].img["title"]] = head[i].a["href"]
    return key.items()
def techhindu():
    page_soup = open_page("https://www.thehindu.com/sci-tech/technology/")
    container = page_soup.find_all("div", {"class": "main"})
    content = container[4].find_all("div", {"class": "story-card-news"})
    key = {}
    for head in content:
        key[head.h3.a.text] = head.h3.a["href"]
    return key.items()
def techndtv():
    page_soup = open_page("https://gadgets.ndtv.com/?pfrom=home-header-globalnav")
    container = page_soup.find("div", {"class": "nlist bigimglist"})
    data = container.findAll("li")
    key = {}
    for i in range(0, 8):
        key[data[i].a.text] = data[i].a["href"]
    return key.items()

# different templates
def home(request):

    key1 =  scraptmi()
    key2 = scraphindu()
    key3 = scrapndtv()
    key4 = scrapindexp()
    key5 = scrapht()
    key6 = scraptnews18()

    return render(request, 'Home/index.html', {'tmi' : key1,
                                               'hindu' : key2,
                                               "ndtv": key3,
                                               "indexp": key4,
                                               "ht" : key5,
                                               "news18" : key6})

def india(request):
    key1 = indiatmi()
    key2 = indiahindu()
    key3 = indiaht()
    key4 = indiaindexp()
    key5 = indiandtv()
    key6 = indianews18()
    return render(request, "Home/index.html", {"tmi" : key1,
                                               "hindu" : key2,
                                               "ht" : key3,
                                               "indexp" : key4,
                                               "ndtv" : key5,
                                               "news18" : key6})

def world(request):
    key1 = worldtmi()
    key2 = worldht()
    key3 = worldndtv()
    key4 = worldnews18()
    key5 = worldindexp()
    key6 = worldhindu()
    return render(request,"Home/index.html", {"tmi" : key1,
                                              "ht" : key2,
                                              "ndtv" : key3,
                                              "news18" : key4,
                                              "indexp" : key5,
                                              "hindu" : key6})

def entertainment(request):
    key1 = etmi()
    key2 = eht()
    key3 = enews18()
    key4 = eindexp()
    key5 = endtv()
    key6 = ehindu()
    return render(request,"Home/index.html", {"tmi" : key1,
                                              "ht" : key2,
                                              "news18" : key3,
                                              "indexp" : key4,
                                              "ndtv" : key5,
                                              "hindu" : key6})

def life_style(request):
    key1 = lifetmi()
    key2 = lifenews18()
    key3 = lifeindexp()
    key4 = lifeht()
    key5 = lifehindu()
    key6 = lifendtv()
    return render(request, "Home/index.html",{"tmi" : key1,
                                              "news18" : key2,
                                              "indexp" : key3,
                                              "ht" : key4,
                                              "hindu" : key5,
                                              "ndtv" : key6})

def sports(request):
    key1 = sportnews18()
    key2 = sportsindexp()
    key3 = sportsht()
    key4 = sportshindu()
    key5 = sportstmi()
    key6 = sportsndtv()
    return render(request,"Home/index.html", {"news18" : key1,
                                              "indexp" : key2,
                                              "ht" : key3,
                                              "hindu" : key4,
                                              "tmi" : key5,
                                              "ndtv" : key6})

def business(request):
    key1 = businessnews18()
    key2 = buisnesstmi()
    key3 = businessindexp()
    key4 = businessndtv()
    key5 = businessht()
    key6 = businesshindu()
    return render(request, "Home/index.html", {"news18": key1,
                                               "tmi" : key2,
                                               "indexp" : key3,
                                               "ndtv" : key4,
                                               "ht" : key5,
                                               "hindu" : key6})


def technology(request):
    key1 = technews18()
    key2 = techindexp()
    key3 = techtmi()
    key4 = techht()
    key5 = techhindu()
    key6 = techndtv()
    return render(request, "Home/index.html", {"news18": key1,
                                               "indexp" : key2,
                                               "tmi" : key3,
                                               "ht" : key4,
                                               "hindu" : key5,
                                               "ndtv" : key6})
