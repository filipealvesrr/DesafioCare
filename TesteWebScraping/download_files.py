import requests

def downloadFile(url, endereco):
    response = requests.get(url)
    if response.status_code == requests.codes.OK: 
        with open(endereco, 'wb') as file:
            file.write(response.content)
        print(f'[!] Download Finish {endereco}')
    else:
        response.raise_for_status()

def downloadAllFiles(list_of_url):
    for index in range(len(list_of_url)):
        name = f'Anexo {index+1}.pdf'
        downloadFile(list_of_url[index], name)
