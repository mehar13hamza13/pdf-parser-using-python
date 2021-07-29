# importing required modules
import PyPDF2
import re
import fitz
from PIL import Image
import io

finalList = []
numList = []
dateList = []

pdfFile = open('data.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFile)


doc = fitz.open("data.pdf")
alltext = ""
for i in range(240):
    page = doc.load_page(i)
    text = page.get_text()
    alltext+=text
    page.clean_contents()
    for img in page.get_images():
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            try:
                pix.writePNG("images/p%s-%s.png" % (i, xref))
            except Exception as e:
                print(e)
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("images/p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None


dataList = alltext.split('(300)')
re.DOTALL = True
for section in dataList:
     #print(section)
     characters = re.findall("(\n)([0-9]{6})(\n)", section)
     all_section = section.split("\n")
     title = all_section[all_section.index("(732)") + 1]
     #print(all_section)
     before_keyword, keyword, after_keyword = section.partition("(511)")

     number = [a.split(" ")[0] for a in after_keyword.split("\n") if a.split(" ")[0].isdigit() ]
     dates = re.findall("../../....", section)

     if len(dates) > 0:
        actual_date = dates[0]

     print(characters[0])
     print(actual_date)
     print(title)
     print(number)
     print("\n")



'''
final_data = []

for page in range(5):
         pageObj = pdfReader.getPage(page)
         alltext+=pageObj.extractText()




'''