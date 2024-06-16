import os
from groq import Groq
import pyttsx3




engine= pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()


client = Groq(api_key='YOUR API KEY' )

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": ""}

file_path = '/home/shreyas/Ultron/personality.txt'

with open(file_path, 'r') as file:
    file_content = file.read()


system_prompt['content'] = file_content


chat_history = [system_prompt]

def respond(prompt):


    chat_history.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=10000,
                                            temperature=1.2)

    chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
  # Print the response
    print((response.choices[0].message.content))
    talk((response.choices[0].message.content))













