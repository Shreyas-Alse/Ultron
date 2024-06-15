import pyttsx3
import speech_recognition as sr
import sounddevice
from brain import respond 
from apps import cmd_exec


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
            cmd_exec_exec('brave')
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
    else:
        respond(command)
        





