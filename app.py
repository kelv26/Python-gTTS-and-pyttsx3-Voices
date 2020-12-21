import tkinter as tk
import sys
from gttspython import *
from pyttsx3func import *
from pyttsx3.drivers import sapi5

win= tk.Tk()
win.title('Python TTS')
win.geometry('500x500')

class PrintLogger(): #create file like object
    def __init__(self, textbox): #pass reference to text widget
        self.textbox= textbox #keep ref
    
    def write(self, text):
        self.textbox.insert(tk.END,text) #write text to textbox
        #could also scroll to end of textbox here to make sure always visible
    
    def flush(self): #needed for file like object
        pass

def rungTTS():
    text= entry.get()
    speak(text)

def runpyTTSMale():
    text1= entry2.get()
    sayMale(text1)

def runpyTTSFemale1():
    text2= entry3.get()
    sayFemale1(text2)

def runpyTTSFemale2():
    text3= entry4.get()
    sayFemale2(text3)

def runpyTTSFemale3():
    text4= entry5.get()
    sayFemale3(text4)

if __name__ == '__main__':
    def do_something():
        print('i did something')
        win.after(1000, do_something)
    
    label = tk.Label(text="This is a gTTS Sound.")
    label.pack()
    entry = tk.Entry(width=50)
    entry.pack()
    button = tk.Button(text="Start", command=rungTTS)
    button.pack()

    label2 = tk.Label(text="This is a pyttsx3 Sound (Male=David lang=en).")
    label2.pack()
    entry2 = tk.Entry(width=50)
    entry2.pack()
    button2 = tk.Button(text="Start", command=runpyTTSMale)
    button2.pack()

    label3 = tk.Label(text="This is a pyttsx3 Sound (Female=Zira  lang=en).")
    label3.pack()
    entry3 = tk.Entry(width=50)
    entry3.pack()
    button3 = tk.Button(text="Start", command=runpyTTSFemale1)
    button3.pack()

    label4 = tk.Label(text="This is a pyttsx3 Sound (Female=HuiHui  lang=cn.simplified).")
    label4.pack()
    entry4 = tk.Entry(width=50)
    entry4.pack()
    button4 = tk.Button(text="Start", command=runpyTTSFemale2)
    button4.pack()

    label5 = tk.Label(text="This is a pyttsx3 Sound (Female=Tracy lang=hk.sar).")
    label5.pack()
    entry5 = tk.Entry(width=50)
    entry5.pack()
    button5 = tk.Button(text="Start", command=runpyTTSFemale3)
    button5.pack()
    # create instance of file like object
    t = tk.Text()
    t.bind("<Key>", lambda e: "break") #Make textbox Read only
    t.pack()
    
    pl = PrintLogger(t)

    # replace sys.stdout with our object
    sys.stdout = pl

    win.mainloop()