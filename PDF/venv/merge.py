import PyPDF2
import sys

first_pdf = sys.argv[1]
second_pdf = sys.argv[2]
third_pdf = sys.argv[3]

with open('new.pdf','wb') as myfile:
    new_file = PyPDF2.PdfFileMerger() #create pdf file merger object
    new_file.append(first_pdf) #append thhe file to the object
    new_file.append(second_pdf)
    new_file.append(third_pdf)
    new_file.write(myfile) #write to the merge pdf