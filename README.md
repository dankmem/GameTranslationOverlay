# GameTranslationOverlay
This is a simple overlay for translating text in games. The primary goal is for translating league of legends korea to english, but it should work for other games with minor adjustments. 
Uses tkinter for overlay. (USE AT OWN RISK, some games anticheat don't allow overlays. Tested to be OK in league of legends)

How to use

Install python https://www.python.org/downloads/ and enable checkbox to set enviromental variable inside installer

Install tesseract-OCR from https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows enable checkbox for additional language data. 

Set tesseract path in system enviromental variables.

Download this repository as zip and extract

Modify translationoverlay.py to adjust settings your prefrences 

  chatbox x1, y1, x2, y2 using coordinates. Default should be fine for default league of legends chat box placement on 1080p
  
  screenshot key(= by default) and other settings.
  
  Text color/font, sizing, location. 


After launching and you see tk inter window/test overlay go in game and when there is chat you want to translate press enter to open chat box and then press your screenshot key (= default). The application should screenshot your chat box region, extract the in game text, send it to google for translation then the overlay window should update to show the translated text. 


TODO
Color whitelisting and better OCR results
Local translation database?
Cleaner Overlay
Easier use for non technical people. 
Update notifications/auto update?
