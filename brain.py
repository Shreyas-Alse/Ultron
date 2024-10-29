import os
from groq import Groq
import pyttsx3




engine= pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

client = Groq(api_key= os.environ.get('MIND_STONE'))

system_prompt = {
    "role": "system",
    "content": ""}

file_path = '/home/shreyas/Ultron/Ultron/personality.txt' # Replace path with yours

with open(file_path, 'r') as file:
    file_content = file.read()


system_prompt['content'] = file_content


chat_history = [system_prompt]

def respond(prompt):


    chat_history.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=500,
                                            temperature=1.8)

    chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
  # Print the response
    print('Ultron:', (response.choices[0].message.content))
    talk((response.choices[0].message.content))











