import pyttsx3
import speech_recognition as sr
import sounddevice
from brain import respond 
from apps import cmd_exec
from brain import talk
from screenreader import screen_read
import os

listener = sr.Recognizer()



def take_command():
    command= ""
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        
    except:
        pass
    return command

def runUltron():
    command=take_command()
    if command == '':
        print("")
    
    elif 'open' in command:
        if 'spotify' in command:
            cmd_exec('spotify')
        elif 'brave' in command:
            cmd_exec('brave')
        elif 'file manager' in command:
            cmd_exec('dolphin')
        elif 'cinema' in command:
            cmd_exec('stremio')
        elif 'terminal' in command:
            cmd_exec('konsole')
        elif 'code' in command:
            cmd_exec('code')
        else:
            respond(command)
    
    elif 'shutdown' in command:
        talk('I am about to shutdown the system, Is it ok?')
        take_command()
        if 'yes' in command:
            talk('initiating shutdown')
            cmd_exec('shutdown -h now')
        else:
            talk('Shutdown Aborted')
    elif 'screen' in command:
        if 'what' in command:
<<<<<<< HEAD
            screen_read()
        elif 'my' in command:
            screen_read()
=======
            scr_content= screen_read()
            respond(scr_content)
            os.remove('/home/shreyas/Ultron/screenshot.png')
        elif 'my' in command:
            scr_content=screen_read()
            respond(scr_content)
            os.remove('/home/shreyas/Ultron/screenshot.png')
>>>>>>> cda5e7718c861f4d94b24bdc416e41beebec4d38
        else:
            respond(content)
    elif 'what' in command:
        if 'this' in command:
<<<<<<< HEAD
            screen_read()
=======
            scr_content=screen_read()
            respond(scr_content)
            os.remove('/home/shreyas/Ultron/screenshot.png')
>>>>>>> cda5e7718c861f4d94b24bdc416e41beebec4d38
        else:
            respond(command)

    else:
        respond(command)
        





