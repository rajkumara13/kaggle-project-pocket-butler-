import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    return f"SPEAK: {text}"

