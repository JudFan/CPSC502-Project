

import os

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pathlib import Path

interpretedString = ''


def voice_input(software):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice_output("How may I help?", 0)
        audio = r.listen(source)
        voice_output("Let me think about that", 0)

        # add function to control when the listen method stops

    match software:
        # recognize speech using Sphinx
        case "sphinx":
            try:
                interpretedString = r.recognize_sphinx(audio)
                print("Sphinx thinks you said " + interpretedString)
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

        case "google":
            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                interpretedString = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said " + interpretedString)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        case "whisper":
            # recognize speech using whisper
            try:
                interpretedString = r.recognize_whisper(audio, language="english")
            except sr.UnknownValueError:
                print("Whisper could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Whisper; {e}")

    return interpretedString
            
            



"""
# recognize speech using Google Cloud Speech
# Before run, create local authentication credentials (``gcloud auth application-default login``)
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
"""

"""
# recognize speech using Whisper API
OPENAI_API_KEY = "INSERT OPENAI API KEY HERE"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
try:
    print(f"OpenAI Whisper API thinks you said {r.recognize_openai(audio)}")
except sr.RequestError as e:
    print(f"Could not request results from OpenAI Whisper API; {e}")
    """

def voice_output(text, printBool):
    text = ".\nSo\n" + text
    myobj = gTTS(text=text, lang='en', slow=False)
    # Saving the converted audio in a mp3 file named
    myobj.save("output1.mp3")
    # Playing the converted file
    playsound("output1.mp3")
    if(printBool == 1):
        print("\nResponse: " + text)

    try:
        Path("output1.mp3").unlink(missing_ok=True)
    except PermissionError:
        print()
    except OSError as e:
        print()

"""        
if(interpretedString1 != ""):
    myobj = gTTS(text=interpretedString1, lang='en', slow=False)
    # Saving the converted audio in a mp3 file named
    myobj.save("output1.mp3")
    print("TTS saying what you said: " + interpretedString1)
    # Playing the converted file
    playsound("output1.mp3")


if(interpretedString2 != ""):
    myobj2 = gTTS(text=interpretedString2, lang='en', slow=False)
    # Saving the converted audio in a mp3 file named 
    myobj2.save("output2.mp3")
    print("TTS saying what you said: " + interpretedString2)
    # Playing the converted file
    playsound("output2.mp3")


if(interpretedString3 != ""):
    myobj3 = gTTS(text=interpretedString3, lang='en', slow=False)
    # Saving the converted audio in a mp3 file named
    myobj3.save("output3.mp3")
    print("TTS saying what you said: " + interpretedString3)
    # Playing the converted file
    playsound("output3.mp3")
"""

def main():
    voice_input("whisper")


if __name__ == "__main__":
    main()