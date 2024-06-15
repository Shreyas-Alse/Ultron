import subprocess
import os
from brain import talk


def cmd_exec(app):

    text= 'opening', app
    print(text)
    talk(text)
    subprocess.Popen([app],
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL,
                     stdin=subprocess.DEVNULL,
                     preexec_fn=os.setsid)



