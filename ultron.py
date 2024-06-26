import pyttsx3
import speech_recognition as sr
import sounddevice
from brain import respond 
from apps import cmd_exec
from brain import talk
from screenreader import screen_read
import os
from apps import open_site
import webbrowser
from speed_test import test_speed


listener = sr.Recognizer()



def take_command():
    command= ""
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('You said:', command)
        
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
        elif 'vivaldi' in command:
            cmd_exec('vivaldi')
        elif 'file manager' in command:
            cmd_exec('dolphin')
        elif 'cinema' in command:
            cmd_exec('stremio')
        elif 'terminal' in command:
            cmd_exec('konsole')
        elif 'code' in command:
            if 'your' in command:
                open_site('https://github.com/Shreyas-Alse/Ultron')
            else:
                cmd_exec('code')
        elif 'github' in command:
            open_site('https://github.com')
        elif 'youtube' in command:
            open_site('https://youtube.com')
        elif 'browser' in command:
            cmd_exec('chromium')
        else:
            respond(command)
    elif 'play' in command:
        url = "https://www.youtube.com/results?search_query=" + command.replace("play", "+")
        webbrowser.open(url)
        respond(command)
    elif 'show' in command:
        url = "https://www.youtube.com/results?search_query=" + command.replace("play", "+")
        webbrowser.open(url)
        respond(command)
    elif 'get' in command:
        url = "https://www.google.com/search?q=" + command.replace("get", "+")
        webbrowser.open(url)
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
            screen_read()
        elif 'my' in command:
            screen_read()
        elif command == '':
            talk('There is nothing significant on your screen')
        else:
            respond(command)
    elif 'what' in command:
        if 'this' in command:
            screen_read()
        elif 'internet speed' in command:
            test_speed()
        else:
            respond(command)
    elif 'help' in command:
        if 'this' in command:
            screen_read()
        else:
            respond(command)
    elif 'run' in command:
        if 'speed test' in command:
            test_speed()
        else:
            respond(command)

    else:
        respond(command)
        





