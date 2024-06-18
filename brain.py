import os
from groq import Groq
import pyttsx3




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

    

    

# Lines to write to the file
lines = [
    "Line 1: Hello, this is the first line.",
    "Line 2: This is the second line.",
    "Line 3: And this is the third line."
]

# Specify the file name
file_name = "example.txt"

# Open the file in write mode ('w')
with open(file_name, 'w') as file:
    # Write each line to the file with a newline character at the end
    for line in lines:
        file.write(line + '\n')

print(f"Content written to {file_name}")








