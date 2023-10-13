League of Legends Translator
![Screenshot](https://github.com/dankmem/GameTranslationOverlay/blob/main/preview%20translation/image.png)
Make sure you are using borderless-windowed or the overlay/screenshots will not work!!!!!

Default key to translate is =

Default key to exit program is f12

edit parts of main.py near the top to change settings. May add settings file and gui later.
      You can edit font size, overlay location/tesseract screenshot region. Use checkbox in options window to show mouse coordinates. Coordinates in main.py are for top left corner and bottom right corner, defaults should work for 1080p default chat box location in league of legends.

# GameTranslationOverlay
This app is primarily meant for translating Korean to English for league of legends players.

Please provide feedback to trihard7#8793 on Discord if you use this! Especially if you are a streamer!
If you window capture in OBS, use the "Windows 10" method to avoid issues.

This is a simple overlay for translating text in games. The primary goal is for translating league of legends korea to english, but it should work for other games with minor adjustments. 
Uses tkinter for overlay. (USE AT OWN RISK, some games anticheat don't like overlays or pyautogui library. May remove pyautogui in future. Tested to be OK in league of legends)
This does not read game memory or use automated inputs, so only really shitty anticheats would false ban for this.

How to use

Install python https://www.python.org/downloads/ and enable checkbox to set enviromental variable inside installer

Install tesseract-OCR from https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows enable checkbox for additional language data. MAKE SURE PATH ENVIROMENTAL VARIABLE IS SETUP FOR TESSERACT OCR OR YOU WILL GET AN ERROR!

Set tesseract path in system enviromental variables.

Download this repository as zip and extract

Run install requirements.bat or open cmd in project folder and type pip install -r requirements.txt

This will install python dependencies for this project if successful. * If you see an error about command pip not found, ensure your python PATH enviromental variable is set correctly.

open run translator.bat or open cmd and type python main.py * If you see an error about command python not found, ensure your python PATH enviromental variable is set correctly.


Modify translationoverlay.py to adjust settings your prefrences 

        chatbox x1, y1, x2, y2 using coordinates. Default should be fine for default league of legends chat box placement on 1080p
  
         screenshot key(= by default) and other settings.
  
         color/font, sizing, location. 


After launching and you see tk inter window/test overlay go in game and when there is chat you want to translate press enter to open chat box and then press your screenshot key (= default). The application should screenshot your chat box region, extract the in game text, send it to google for translation then the overlay window should update to show the translated text. 


TODO
Color whitelisting and better OCR results

Local translation database?

Better overlay

More languages

Save/Load settings file/GUI settings/saving settings quality of life of non technical people

auto update?

translate clipboard, if it can be accessed in game. (need to test)
