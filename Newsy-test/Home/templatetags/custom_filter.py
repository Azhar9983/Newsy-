from django import template
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen as ureq

register = template.Library()

@register.filter
def splitH(value):
    key = value.split('*&*')
    return key[0]

@register.filter
def splitL(value):
    key = value.split('*&*')
    return key[1]

@register.filter
def popnews(value, news):
    if news == "tmi" :
        request = Request(value, headers={'User-Agent': 'Mozilla/5.0'})
        uclient = ureq(request)
        page_html = uclient.read()
        uclient.close()
        page_soup = soup(page_html,'html.parser')
        container = page_soup.find("ul", {"class": "_223qM"})
        try:
            return container.li.text
        except AttributeError:
            try:
                container = page_soup.find("section", {"class": "highlight clearfix vdo"})
                return container.ul.li.text
            except AttributeError:
                try:
                    container = page_soup.find("section", {"class": "highlight clearfix"})
                    return container.ul.li.text
                except AttributeError:
                    return "Loading...."
    else :
        return "..."
