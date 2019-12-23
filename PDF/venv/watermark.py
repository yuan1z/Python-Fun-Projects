import PyPDF2
with open('new.pdf','rb') as myfile:
    reader = PyPDF2.PdfFileReader(myfile)  # create a pdf reader object
    with open('wtr.pdf','rb') as mark:
        marker = PyPDF2.PdfFileReader(mark)  # create a pdf marker reader object
        marker_page = marker.getPage(0) #create a marker page object
        writer = PyPDF2.PdfFileWriter()  # create a writer object
        #get each page of the new.pdf and merge page using marker object, add the merged page to the writer object
        for i in range(int(reader.numPages)):
            page = reader.getPage(i)
            page.mergePage(marker_page)
            writer.addPage(page)
        # write the writer object to the new file
        with open("draft.pdf", 'wb') as write_file:
            writer.write(write_file)