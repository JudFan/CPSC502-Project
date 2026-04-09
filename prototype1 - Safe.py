import CPSC502_Voice_Interface as voice
import requests
import openai
from pynput import keyboard
import sys

import os

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound



def main():

    needVisualAid = False

    spokenInput = voice.voice_input("whisper") 
    prefaceString = "You are a pair programmer, acting as the observer/navigator role. Do not make code for me. Exclude \' from your response. I just need high level feedback on my query/code\n"
    prefaceString2 = "\n\n Here is my query:\n"

    file_path = sys.argv[1] 
    code = ''
    with open(file_path, 'r') as f:
        code = f.read()

    
    codeLineByLine = code.split("\n")

    codeUpdated = ''

    for i in range(0,len(codeLineByLine)):
        codeLineByLine[i] = "Line " + str(i+1) + ":" + codeLineByLine[i]
        codeUpdated += codeLineByLine[i] + "\n"
    

    highlightedCode = ''
    try:
        highlightedCode = "\n\nFocus on this highlighted code: \n" + sys.argv[2]
    except:
        highlightedCode = ''

    visualAid = ''
    if not needVisualAid:
        visualAid = '\n\nPlease refer to code using line numbers. My code, starting from Line 1 starts below:\n'

    
    previousContext = sys.argv[3]
    previousContextStatement = ''
    if(previousContext != ''):
        previousContextStatement = "This is our conversation history so far:\n"


    # Buy a liscence from ChatGPT to make this program work in the first place
    # Preemptive prompt to get AI to make its own code and store it, and then use that as reference to coach student in coding further
    # Make repetitive reminders by AI to keep user in track
    # make the program active all the time, functions activate on keybind.
    # introduce a module that detects what lines in the code file you wish to query (grab highlighted text)
    # find pointer of the active cursor (Aka the blinking "|") in the IDE to find code block to analyse.

    input_string = prefaceString + previousContextStatement + previousContext + visualAid + codeUpdated + prefaceString2 + spokenInput + highlightedCode
    context = visualAid + codeUpdated + prefaceString2 + spokenInput + highlightedCode

    print("\nUser Prompt:\n", context)

    
    client = openai.OpenAI(
        # Insert your own API Key
        api_key=''
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": input_string,
            },
        ],
    )

    result = completion.choices[0].message.content
    result = result.replace("`", "")
    result = result.replace("_", "")
    result = result.replace("Response:", "")
    voice.voice_output(result, 1)



if __name__ == "__main__":
    main()
    sys.stdout.flush()