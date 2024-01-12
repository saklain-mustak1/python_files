import pyttsx3
speaker = pyttsx3.init()
text=input("write something: ")
speaker.say(text)
speaker.runAndWait()
