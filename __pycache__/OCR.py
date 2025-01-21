# Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki.
# Install this exe in C:\Program Files (x86)\Tesseract-OCR
# Open virtual machine command prompt in windows or anaconda prompt.
# Run pip install pytesseract
# To test if tesseract is installed type in python prompt:
# import pytesseract
# print(pytesseract)
# if get error 'pytesseract.pytesseract.TesseractNotFoundError: C:\Program Files (x86)\Tesseract-OCR\tesseract.exe is not installed or it's not in your PATH. See README file for more information.'
# go to https://www.youtube.com/watch?v=m8idoiFrIgw



import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\66869\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
parent_dr = os.getcwd()
#print("current path" , parent_dr)

allfile = os.listdir(parent_dr)
#print("Filelist", allfile)

imagelist = []
for a in allfile:
    if os.path.isfile(a) and a.startswith("ocr") and a.endswith (".jpg"):
        imagelist.append(a)
print(imagelist)

def scanImage():
    text = pytesseract.image_to_string(imagelist[0])
    print(text)

scanImage()     