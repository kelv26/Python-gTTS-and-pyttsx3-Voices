import pyttsx3

engine= pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 150)

def sayMale(text):
    #Set the voice of the bot
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    print('David: ',text)
    engine.say(text)
    engine.runAndWait()

def sayFemale1(text):
    #Set the voice of the bot
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    print('Zira: ',text)
    engine.say(text)
    engine.runAndWait()

def sayFemale2(text):
    #Set the voice of the bot
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) 
    print('HuiHui: ',text)
    engine.say(text)
    engine.runAndWait()

def sayFemale3(text):
    #Set the voice of the bot
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id) 
    print('Tracy: ',text)
    engine.say(text)
    engine.runAndWait()

#Show available voices
# voices=engine.getProperty('voices')
# for voice in voices:
#     print(voice)

