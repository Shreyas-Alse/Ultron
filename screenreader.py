import mss
import mss.tools
import subprocess
import pytesseract
import os
from brain import respond
from PIL import Image


def screen_read():
    try:
        with mss.mss() as sct:
            screenshot = sct.shot(output='screenshot.png')
        image = Image.open("screenshot.png")
        text = pytesseract.image_to_string(image)
        respond(text)
    except:

        subprocess.run(['spectacle', '-b', '-o', 'screenshot.png'], check=False)
        image = Image.open("screenshot.png")
        text = pytesseract.image_to_string(image)
        respond(text)

