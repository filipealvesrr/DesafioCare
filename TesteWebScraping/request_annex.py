import requests 
from bs4 import BeautifulSoup

def fetchWebPage(url):
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.OK:
            return response.text
        else:
            print('[!] REQUEST ERROR')
    except Exception as error:
        print('[!] REQUEST ERROR')
        print(error)

def parsingTextFromWeb(response_web_page):
    try:
        web_page = BeautifulSoup(response_web_page, 'html.parser')
        return web_page
    except Exception as error:
        print('[!] Parsing HTML Error')
        print(error)

def extractLinks(url):
    site_text = fetchWebPage(url)
    if site_text:
        web_page = parsingTextFromWeb(site_text)
        links = web_page.findAll('a', attrs={'class': 'internal-link'})
        right_links = [links[1]['href'], links[3]['href'], links[4]['href'], links[5]['href']]
        return right_links
    else:
        print('[!] No content')