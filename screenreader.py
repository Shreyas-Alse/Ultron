import mss
import mss.tools
from PIL import Image
import pytesseract
import os
<<<<<<< HEAD
from brain import respond

=======
>>>>>>> cda5e7718c861f4d94b24bdc416e41beebec4d38

def screen_read():
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')
    image = Image.open("screenshot.png")
    text = pytesseract.image_to_string(image)
<<<<<<< HEAD
    respond(text)
    try:
        os.remove('/home/shreyas/Ultron/screenshot.png')
    except:
        pass
    
    
=======
    return(text)
    os.remove('/home/shreyas/Ultron/screenshot.png')
>>>>>>> cda5e7718c861f4d94b24bdc416e41beebec4d38

