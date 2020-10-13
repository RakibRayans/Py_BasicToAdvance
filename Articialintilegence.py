import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything....")
    audio = r.listen(source)

    print("voice to text:\n" + sr.recognize_google(paudio))