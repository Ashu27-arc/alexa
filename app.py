import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a voice command and return it as text."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run_alexa():
    """Process the given command."""
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {time}")
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, sentences=1)
        talk(info)
    elif "who are you" in command:
        talk("I am your assistant Alexa, here to help you.")
    elif "are you single" in command:
        talk("I am in a relationship with WiFi.")
    elif "tell me a joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("I didn't catch that. Please say the command again.")

# Run the assistant in an infinite loop
while True:
    run_alexa()
