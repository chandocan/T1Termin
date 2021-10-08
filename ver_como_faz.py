import aiml
import pyttsx
import pyaudio
import speech_recognition as sr
import os

kernel = aiml.Kernel()

r = sr.Recognizer()

engine = pyttsx.init('espeak')
rate = engine.getProperty('rate')

engine.setProperty('rate', rate-50)

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# Press CTRL-C to break this loop
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("You said : " + r.recognize_google(audio))
        input = r.recognize_google(audio)
#       input = raw_input("Enter your message >> ")
        response = kernel.respond(input)
        print response
        engine.say(response)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("I could not understand what you just said")
    except sr.RequestError as e:
        print("Could not request results".format(e))       self.janela['_BODY_'].update(value=file.read_text())
            self.janela['_INFO_'].update(value=file.absolute())
        return file
