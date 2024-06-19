import subprocess
import os
from brain import talk
import webbrowser


def cmd_exec(app):

    text= 'opening', app
    print(text)
    talk(text)
    subprocess.Popen([app],
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL,
                     stdin=subprocess.DEVNULL,
                     preexec_fn=os.setsid)


def open_site(url):
    text = 'opening', url
    talk(text)
    webbrowser.open(url)

