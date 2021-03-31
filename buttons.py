from gpiozero import Button
from signal import pause

def handleButton(button):
    print(button.pin)

key1 = Button(5)
key2 = Button(6)
key3 = Button(13)
key4 = Button(19)

key1.when_pressed = handleButton
key2.when_pressed = handleButton
key3.when_pressed = handleButton
key4.when_pressed = handleButton

pause()