import requests 
from bs4 import BeautifulSoup

LINK_URL = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

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
        soup = BeautifulSoup(response_web_page, 'html.parser')
        return soup
    except Exception as error:
        print('[!] Parsing HTML Error')
        print(error)

def extractLinks():
    site_text = fetchWebPage(LINK_URL)
    if site_text:
        soup = parsingTextFromWeb(site_text)
        links = soup.findAll('a', attrs={'class': 'internal-link'})
        right_links = [links[1]['href'], links[3]['href'], links[4]['href'], links[5]['href']]
        return right_links
    else:
        print('[!] No content')

def downloadFile(url, endereco):
    response = requests.get(url)
    if response.status_code == requests.codes.OK: 
        with open(endereco, 'wb') as file:
            file.write(response.content)
        print("Download Finish")
    else:
        response.raise_for_status()

def downloadAllFiles(list_of_url):
    for index in range(len(list_of_url)):
        name = f'Anexo {index+1}.pdf'
        downloadFile(list_of_url[index], name)

#fetchWebPage(LINK_URL)
#downloadFile(list_of_url[0], 'teste.pdf')
list_of_url = extractLinks()
downloadAllFiles(list_of_url)