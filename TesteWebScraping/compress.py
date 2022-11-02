import zipfile

def compressForZip(list_of_docs):
    file_zip_compress = zipfile.ZipFile('Annex_compress.zip', 'w', zipfile.ZIP_DEFLATED)
    
    for index in range(len(list_of_docs)):
        name = f'Anexo {index + 1}.pdf'
        file_zip_compress.write(name)
    
    file_zip_compress.close
    print('[!] Compression done successfully')
