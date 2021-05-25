import os
import tesseract
from PIL import Image
tesseract.tesseract.tesseract_cmd=r"c:\users\shuvo\appdata\local\pip\cache\wheels\6c\c5\81\8310cc52076953e53412ed1875a5e224c92940235bdcee21a2"
def converter():
    img=Image.open('img.jpg')
    text=tesseract.image_to_string(img)
    print(text)
converter()