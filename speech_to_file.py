import speech_recognition as sr 
import pyttsx3
from gtts import gTTS
import os
r = sr.Recognizer()
def speakout(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait() 
def save_file(mytext):
    file_input = input("Enter a file name  : ")
    audio_file = (file_input+".mp3")
    os.mkdir(file_input) 
    os.chdir(os.getcwd()+'/'+file_input)  
    myobj.save(audio_file)
    os.system(audio_file)
    txt_file = open(file_input+".txt","w")
    txt_file.write(mytext)
    txt_file.close()
    exit(0)
speakout('hi sir, welcome') 
with sr.Microphone() as source:
    speakout("Say something!")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        myobj = gTTS(text=text, lang='en', slow=False)
        speakout('You said, '+text)
        print('You said: {}'.format(text))
        a = input("\nSave and then collect the files from directory\nDo you want to save as a audio file(y/n) : ")
        if a == 'y' or a == 'Y':
            save_file(format(text))
        else:
            a = input("Press 0 to close : ")
            exit(0)   
    except:
        print('Sorry  could not recognize your voice')
    