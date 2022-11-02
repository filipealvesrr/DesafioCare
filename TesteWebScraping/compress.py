import zipfile

z = zipfile.ZipFile('Arqteste', 'w', zipfile.ZIP_DEFLATED)
z.write('Anexos Concatenados.pdf')
z.write('Anexo 1.pdf')
z.close
