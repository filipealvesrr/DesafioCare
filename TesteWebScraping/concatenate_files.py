import PyPDF2  

file1 = open('Anexo 1.pdf', 'rb')
file2 = open('Anexo 2.pdf', 'rb')
file3 = open('Anexo 3.pdf', 'rb')
file4 = open('Anexo 4.pdf', 'rb')

data_file1 = PyPDF2.PdfFileReader(file1)
data_file2 = PyPDF2.PdfFileReader(file2)
data_file3 = PyPDF2.PdfFileReader(file3)
data_file4 = PyPDF2.PdfFileReader(file4)

merge = PyPDF2.PdfFileMerger()
merge.append(data_file1)
merge.append(data_file2)
merge.append(data_file3)
merge.append(data_file4)

merge.write('Anexos Concatenados.pdf')


