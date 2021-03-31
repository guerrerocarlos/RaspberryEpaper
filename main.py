import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in7b
from PIL import Image
import time
from gpiozero import Button
from signal import pause

GPIO.setmode(GPIO.BOARD)
epd = epd2in7b.EPD()
epd.init()

def handleButton(button):
    if button.pin == 5:
        print("Clearing screen..")
        clearScreen()
    elif button.pin == 6:
        print("Colour image...")
        colourScreen()
    else:
        exitProgram()

def clearScreen():
    epd.Clear()
    time.sleep(1)

def colourScreen():
    HBlackimage = Image.open(os.path.join(picdir, '2in7b-b.bmp'))
    HRedimage = Image.open(os.path.join(picdir, '2in7b-r.bmp'))
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
    time.sleep(2)

def exitProgram():
    epd.sleep()
    sys.exit



key1 = Button(5)
key2 = Button(6)
key3 = Button(13)
key4 = Button(19)

key1.when_pressed = handleButton
key2.when_pressed = handleButton
key3.when_pressed = handleButton
key4.when_pressed = handleButton

pause()
