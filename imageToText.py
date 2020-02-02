import pytesseract as tess
import re
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image





img = Image.open('samplefir.txt_2.png')
text = tess.image_to_string(img)
strr = text.split('\n')
mydict={}
for st in strr:
    s = st.split(':')
    if len(s) > 1:
        sx = re.findall("[a-zA-Z]", s[0])  
        key = ''.join([str(elem) for elem in sx]) 
        mydict[key]=s[1]
    
        
print(mydict)
