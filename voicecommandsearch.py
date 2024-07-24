#tell the website with extension
import speech_recognition as sr
import webbrowser

r = sr.Recognizer()
r.energy_threshold = 5000
with sr.Microphone() as source:
    print("Please speak the website name loudly....")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        text_for_url = '+'.join(text.split())
        url = 'https://www.' + text_for_url   
        webbrowser.open(url)
    except:
        print("Can't Recognize your voice please")