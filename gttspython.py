from gtts import gTTS
from playsound import playsound
import time
import os
import os.path

"""This function will take a string as input
convert it into voice and save it as a file temp.mp3
play it and delete it"""
def speak(temps):
    tts = gTTS(temps, lang="en")

    if not os.path.exists("/temp"):
        os.makedirs("/temp")
        print("Please try again. (created 'temp' folder for Google .mp3 files.")
    else:
        print('gTTS: ',temps)
        tts.save("/temp/temp1.mp3")
        playsound('/temp/temp1.mp3')
        time.sleep(0.2)
        os.remove("/temp/temp1.mp3")
    