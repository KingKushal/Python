import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Dvid: ", audio)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    

    else:
        speak("Good evening")


    speak("I am siri sir  please tell me how may i help")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='an-in')
        


    except Exception as e:
        # print(e)
        print("say that again please....")
        # speak("say that again please....")
        return "None"
    return query

if __name__ =="__main__":
    wishme()
    while True:
        query = takecommand().lower()



    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")


        # elif 'playmusic' in query:
        #     music_dir = location of directory
        # range = os.listdir(music_dir)
        # print(songs)
        # os.startfile(path.join(music_dir, songs[0]))

        elif 'what is the time siri' in query:
            Time = str(datetime.datetime.now().strftime("%H:%M:%S"))
            print(f"Sir, the time is" + Time)

        elif 'open code' in query:
            codePath ="C:\\Users\\STPL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)

        elif 'open edge' in query:
            edgePath ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" 
            os.startfile(edgePath)
        elif 'open WhatsApp' in query:
            whatsappPath = "C:\\Users\\STPL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsappPath)
        elif 'open brave' in query:
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" 
            os.startfile(bravePath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open python playlist' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
        elif 'open class' in query:
            webbrowser.open("https://meet.google.com/zir-fdye-fry")
        elif 'open science class' in query:
            webbrowser.open("https://meet.google.com/pey-kuiq-ciq")
        elif 'open computer class' in query:
            webbrowser.open("https://meet.google.com/wic-njzg-szb")
        elif 'open java playlist' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9ajyk081To1Cbt2eI5913SsL")

        elif 'open python' in query:
            pythonPath = "C:\\python3.9\\Lib\\idlelib\\idle.pyw"
            os.startfile(pythonPath)

        elif 'play song rata lambiya' in query:
            webbrowser.open("https://www.youtube.com/watch?v=orYf6VDtj_k")

        elif 'names of my parents' in query:
            speak("Arinjay dadhich is your father And Premlata sharma is your mother")

        elif 'contact of my uncle' in query:
            speak("contact is 90244 33346")

        elif 'contact of my aunty' in query:
            speak("contact is 96949 12713")

        elif 'contact of my grandpa' in query:
            speak("contact is  90248 49611")

        elif 'contact of my grandma' in query:
            speak("contact is 94608 96873")

        elif 'contact of my brother' in query:
            speak("contact is 94608 96873")

        elif 'contact of my father' in query:
            speak("contact is 70145 80626")

        elif 'contact of my mother' in query:
            speak("contact is 95115 20317")

        elif 'names of my friends' in query:
            speak("dhairya  kushal  udit  dharam")

        elif 'pincode of my area' in query:
            speak("302026")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in")    

        

        

        elif 'bye' in query:
            break
        else:
            continue
        
