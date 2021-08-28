# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('Power Transmission.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.
 
from_page = pdfReader.getNumPages()
speak = pyttsx3.init()
for i in range(1,from_page):
    page=pdfReader.getPage(i)
# extracting the text from the PDF
    text = page.extractText()
    print(text)
# reading the text

    speak.say(text)
    speak.runAndWait()







    