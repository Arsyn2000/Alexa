import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Recognises your voice
listener = sr.Recognizer()
engine = pyttsx3.init()
# Selecting a female voice from 2 available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def alexa_greetings():
    # The initial statements said by Alexa
    print("Alexa: I am Alexa. What can I do for you?")
    engine.say("I am Alexa. What can I do for you?")


def alexa_talks(text):
    engine.say(text)


def user_talks():
    # Recording our response and converting it into text
    try:
        # Asking the listener to listen to the source
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            # Audio to text
            command = listener.recognize_google(voice)
            print("Length of Commad:", len(command))
            if len(command) != 0:
                print("User:", command)
    except:
        pass
    if len(command) != 0:
        return command
    else:
        return ""


def run_alexa():
    command = user_talks()
    if "play" in command:
        command = command.replace('play', '')
        print("Alexa: Playing" + command)
        alexa_talks("Playing" + command)
        pywhatkit.playonyt(command)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print("Alexa: Current time is " + time)
        alexa_talks("Current time is " + time)
    elif "joke" in command:
        print("In tell me a joke")
        joke = pyjokes.get_joke()
        print(joke)
        alexa_talks(joke)
    elif "wikipedia" or "wiki" or "search" or "find" or "who is" or "what is" in command:
        person = ""
        if "wikipedia" in command:
            person = command.replace("wikipedia", "")
        if "wiki" in command:
            person = command.replace("wiki", "")
        if "search" in command:
            person = command.replace("search", "")
        if "find" in command:
            person = command.replace("find", "")
        if "who is" in command:
            person = command.replace("who is", "")
        if "what is" in command:
            person = command.replace("what is", "")
        if len(person) != 0:
            info = wikipedia.summary(person, 3)
            print(info)
            alexa_talks(info)
        else:
            print("Please say it again in wiki.")
    else:
        print("Please say it again.")
        alexa_talks("Please say it again.")


if __name__ == "__main__":
    while True:
        run_alexa()
