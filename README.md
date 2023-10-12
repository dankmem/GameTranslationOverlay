# GameTranslationOverlay
This app is primarily meant for translating Korean to English for league of legends players.

Please provide feedback to trihard7#8793 on Discord if you use this!
Especially useful for twitch streamers.

This is a simple overlay for translating text in games. The primary goal is for translating league of legends korea to english, but it should work for other games with minor adjustments. 
Uses tkinter for overlay. (USE AT OWN RISK, some games anticheat don't allow overlays. Tested to be OK in league of legends)

How to use

Install python https://www.python.org/downloads/ and enable checkbox to set enviromental variable inside installer

Install tesseract-OCR from https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows enable checkbox for additional language data. 

Set tesseract path in system enviromental variables.

Download this repository as zip and extract

Open cmd window in the folder you extract to.

Type "pip install -r requirements.txt"

This will install python dependencies for this project if successful. * If you see an error about command pip not found, ensure your python PATH enviromental variable is set correctly.

Modify translationoverlay.py to adjust settings your prefrences 

        chatbox x1, y1, x2, y2 using coordinates. Default should be fine for default league of legends chat box placement on 1080p
  
         screenshot key(= by default) and other settings.
  
         color/font, sizing, location. 


After launching and you see tk inter window/test overlay go in game and when there is chat you want to translate press enter to open chat box and then press your screenshot key (= default). The application should screenshot your chat box region, extract the in game text, send it to google for translation then the overlay window should update to show the translated text. 


TODO
Color whitelisting and better OCR results

Local translation database?

Cleaner Overlay

Settings file/GUI settings use for non technical people

Update notifications/auto update?
