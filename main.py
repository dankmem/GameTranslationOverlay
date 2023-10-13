# This is a sample Python script.
import time
import tkinter
from tkinter import messagebox, ttk
import googletrans
import cv2
import numpy
import tkinter as tk
import urllib.request
import numpy as np
import pyautogui
from PIL import Image as pilimg
from tkinter import *
import pytesseract
import keyboard
import threading
import dxcam
from googletrans import Translator
from pytesseract import image_to_string

def writecoordcmd():
    x, y = pyautogui.position()
    print(x, y)


#Set overlaybool to false if overlays not allowed in your game
#will move some of these options to tkinter gui eventually.
closekey="f12"
translationkey="="
overlaybool=True
overlayonlygamewindowactive=False
gamewindowname="League of Legends (TM) Client"
overlaylocationx = 65
overlaylocationy = 400
langsrc=""
langtarget=""
textcolor="cyan"
textsize=8
tessoractlang=""



#create tkinter windows
optionswindow = Tk()
optionswindow.title("Options")
optionswindow.geometry("250x150")
translationwindow = tk.Tk()
writecoord = IntVar()
langlabel = tk.Label(optionswindow, text="top=input lang " + "\n" + "bottom = output lang for translate").pack()
textlabel = tk.Label(translationwindow, fg="cyan",bd=0, font=("Georgia", textsize), text="Ready to translate", bg="white", justify="left")
writecoordbox = tk.Checkbutton(optionswindow, text='Show mouse coord',variable=writecoord, onvalue=1, offvalue=0)
coordlabel = tk.Label(optionswindow, fg="black",bd=0, font=("Georgia", textsize), text="X: Y:", justify="left")
inputlangs = ["ko", "en", "zh-CN", "fr", "de", "es", "fil", "vi", "th", "tr", "ml", "ar", "pt-BR", "bg", "cs", "da", "nl", "hi", "ja", "no", "pl", "pt-PT", "ro", "ru", "uk"]
outputlangs = ["en", "ko", "zh-CN", "fr", "de", "es", "fil", "vi", "th", "tr", "ml", "ar", "pt-BR", "bg", "cs", "da", "nl", "hi", "ja", "no", "pl", "pt-PT", "ro", "ru", "uk"]
selectedinputlang = tkinter.StringVar(optionswindow)
selectedinputlang.set("ko")
selectedoutputlang = tkinter.StringVar(optionswindow)
selectedoutputlang.set("en")
inputlangmenu = tkinter.OptionMenu(optionswindow,  selectedinputlang, *inputlangs)
outputlangmenu = tkinter.OptionMenu(optionswindow, selectedoutputlang, *outputlangs)
inputlangmenu.pack()
outputlangmenu.pack()
textlabel.pack()
writecoordbox.pack()
coordlabel.pack()
translationwindow.overrideredirect(overlaybool)
translationwindow.geometry("+"+str(overlaylocationx)+"+"+str(overlaylocationy))
translationwindow.lift()
translationwindow.wm_attributes("-topmost", overlaybool)
translationwindow.wm_attributes("-disabled", overlaybool)
translationwindow.wm_attributes("-transparentcolor", "white")
textlabel.pack()

#initiate translator service
translator = Translator()
translator = Translator(service_urls=['translate.google.com'])

#Initiate window capture
#x, y is top left corner coordinates. x2, y2 is bottom right coordinates
x, y = 60, 640
x2, y2 = 580, 860
screencap = dxcam.create(output_color="RGB")
screencap.start(region=(x, y, x2, y2))

#define functions.
def showimage(imgarray):
    img = pilimg.fromarray(imgarray, "RGB")
   # img.show()
    return
def find_between(text, first, last):
    start = text.find(first) + len(first)
    end = text.find(last, start)
    return text[start:end] if start != -1 and end != -1 else None
def gettext():
    frame = screencap.get_latest_frame()
    if frame is None:
        return
    HSV_img = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(HSV_img)
   # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
   # img2 =  cv2.adaptiveThreshold(gray,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)

    thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
   # pilimg.fromarray(thresh).show()
    img = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    #pilimg.fromarray(thresh, "L").show()
    #pilimg.fromarray(img, "L").show()
    #pilimg.fromarray(gray, "L").show()
   # pilimg.fromarray(img2, "L").show()
    txt = image_to_string(img, lang=getTessInputLang())
    return txt
def gettranslate():
    global langsrc
    global langtarget
    global textcolor
    window = pyautogui.getActiveWindowTitle()

    if overlayonlygamewindowactive and (gamewindowname != window):
        #print(window)
        textlabel.config(text="")
        return

    #print(window)
    if (keyboard.is_pressed("/")):
        frame = screencap.get_latest_frame( )
        imgprocess(frame)
  #  if window != "League of Legends (TM) Client":
    #    root.withdraw()
   # if window == "League of Legends (TM) Client":
     #   root.deiconify()
    #if (keyboard.is_pressed("=") and (window == "League of Legends (TM) Client")):
    if (keyboard.is_pressed(translationkey)):

        text = gettext()
        lines = text.split("\n")
        translatestring= ""
        labeltxt = ""
        for line in lines:
            if len(line) > 5:
                split = line.split("(")
               # line = line.replace('"',' " ')
                #line = line.replace("(", " ( ")
                #line = line.replace(")", " ) ")
                #line = line.replace(':', " : ")
                #line = line.replace("[", " [ ")
                #line = line.replace("]", " ] ")
                #line = line.replace('”', ' " ')
                #if len(split) >= 2:
                  #  print(split[1]," split")
                 #   translatestring= translatestring+split[1] + "\n"
                #if len(split) == 1 or len(split)==0:
                translatestring= translatestring+line+'\n'
        if (len(translatestring) > 3):
            langsrc = selectedinputlang.get()
            langtarget = selectedoutputlang.get()
            translation = str(translator.translate(translatestring, src=langsrc, dest=langtarget))
            result = find_between(translation, "text=", ", pronunciation=None,")
            textlabel.config(text=result)
    return


def getTessInputLang():
    global selectedinputlang
    lang = selectedinputlang.get()
    print(selectedinputlang)
    if lang == "ko":
        return "kor"
    if lang == "en":
        return "eng"
    if lang == "zh-CN":
        return "chi_sim"
    if lang == "fr":
        return "fra"
    if lang == "de":
        return "deu"
    if lang == "es":
        return "spa"
    if lang == "fil":
        return "fil"
    if lang == "vi":
        return "vie"
    if lang == "th":
        return "tha"
    if lang == "tr":
        return "tur"
    if lang == "ml":
        return "mal"
    if lang == "ar":
        return "ara"
    if lang == "pt-BR":
        return "por"
    if lang == "bg":
        return "bul"
    if lang == "cs":
        return "ces"
    if lang == "da":
        return "dan"
    if lang == "nl":
        return "nld"
    if lang == "hi":
        return "hin"
    if lang == "ja":
        return "jpn"
    if lang == "no":
        return "nor"
    if lang == "pl":
        return "pol"
    if lang == "pt-PT":
        return "por"
    if lang == "ru":
        return "rus"
    if lang == "uk":
        return "ukr"
    if lang == "ro":
        return "ron"

    return ""


#not working yet
def replacecolor(img, h,s,v, h2, s2, v2):
    start = time.time()
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (h, s, v), (h2, s2, v2))
    bak = img.copy()
    # replace with red
    bak[mask > 0] = (0, 0, 0)
    end = time.time()
    print(end-start)
    return bak

def imgprocess(img):
    kernel = np.ones((1, 1), np.unint8)
    imgoriginal = img
    img = cv2.resize(img, None, fx=2, interpolation= cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.medianBlur(img, 5)
    #pilimg.fromarray(imgoriginal).show()
   # img2 = replacecolor(img, 1, 1, 1, 200, 200, 200)
   # pilimg.fromarray(img2).show()
    return img

#Update notification
versionfile=open("version.txt", "r")
localversion=float(versionfile.read())
versionfile.close()
try:
    contents = urllib.request.urlopen("https://raw.githubusercontent.com/dankmem/GameTranslationOverlay/main/version.txt").read()
    if contents:
        webversion = float(contents)
        if webversion > localversion:
            tkinter.messagebox.showinfo(title=None, message="Update on github")
            print("Update Availible on github.")
            print("Local Version: " + str(localversion) + " web version: " + str(webversion))
except:
    tkinter.messagebox.showinfo(title=None, message="Could not check github for update...")

#main loop
while True:
    if keyboard.is_pressed("f12"):
        exit()
    x, y = pyautogui.position()
    if writecoord.get() == 1:
        coordlabel.config(text="X:"+str(x) + " Y:"+str(y))
        optionswindow.update()
    gettranslate()
    translationwindow.update()
    time.sleep(0.01)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
