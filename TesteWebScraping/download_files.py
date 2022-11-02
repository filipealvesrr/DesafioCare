import requests 

list_of_url = [
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf', 
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546.pdf', 
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf', 
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf'
              ]

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

downloadAllFiles(list_of_url)