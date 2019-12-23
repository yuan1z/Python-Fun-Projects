import PyPDF2
with open('dummy.pdf','rb') as myfile:
    reader = PyPDF2.PdfFileReader(myfile) #create a pdf reader object
    print(reader.numPages)
    print(reader.getPage(0))
    page = reader.getPage(0) #create page 0 page object
    page.rotateClockwise(180) #rotate page 0 180 degree
    writer = PyPDF2.PdfFileWriter() #create a writer object
    writer.addPage(page) #append the page object to writer object
    with open('tilt.pdf','wb') as newfile:
        writer.write(newfile) #write the writer object to new file
