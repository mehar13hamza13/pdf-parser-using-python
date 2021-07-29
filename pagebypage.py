from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
import io
import os

fp = open(r'data.pdf', 'rb')
rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
print(type(retstr))
codec = 'utf-8'
laparams = LAParams(line_margin=5, char_margin=5)
device = TextConverter(rsrcmgr, retstr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

page_no = 0
for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
    if pageNumber == page_no:
        interpreter.process_page(page)

        data = retstr.getvalue()

        retstr.truncate(0)
        retstr.seek(0)

    page_no += 1
    print(data)
    if page_no==10:
        break