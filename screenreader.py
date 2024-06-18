import mss
import mss.tools
from PIL import Image
import pytesseract
import os
from brain import respond


def screen_read():
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')
    image = Image.open("screenshot.png")
    text = pytesseract.image_to_string(image)
    respond(text)
    try:
        os.remove('/home/shreyas/Ultron/screenshot.png')
    except:
        pass
    
    

