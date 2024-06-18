import mss
import mss.tools
from PIL import Image
import pytesseract
import os

def screen_read():
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')
    image = Image.open("screenshot.png")
    text = pytesseract.image_to_string(image)
    return(text)
    os.remove('/home/shreyas/Ultron/screenshot.png')

