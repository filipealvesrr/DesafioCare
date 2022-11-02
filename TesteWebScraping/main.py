import request_annex
import download_files
import compress

LINK_URL = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

list_of_url = request_annex.extractLinks(LINK_URL)
download_files.downloadAllFiles(list_of_url)
compress.compressForZip(list_of_url)