import os
from groq import Groq
import pyttsx3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



engine= pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()


client = Groq(api_key='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' )

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




writer_mode = {
    "role": "system",
    "content": 'You are a professional writer and write documents on the given topic. No other reponses are to be given. Write elaborately along with links for future further references'}

writer_history= [writer_mode]

    
def prep_doc(topic):

  # Append the user input to the chat history
    writer_history.append({"role": "user", "content": topic})

    response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=writer_history,
                                            max_tokens=10000,
                                            temperature=1.2)
  # Append the response to the chat history
    writer_history.append({
            "role": "Professional Writer",
            "content": response.choices[0].message.content
        })
    doc_content= (response.choices[0].message.content)
    return doc_content








