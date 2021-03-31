from gpiozero import Button
from signal import pause

def handleBtnPress(btn):
    # get the button pin number
    pinNum = btn.pin.number

    # python hack for a switch statement. The number represents the pin number and
    # the value is the message we will print
    switcher = {
        5: "Hello, World!",
        6: "This is my first \nRPi project.",
        13: "Hope you liked it.",
        19: "Goodbye"
    }
    
    msg = switcher.get(btn.pin.number, "Error")
    print(msg)

key1 = Button(5)
key2 = Button(6)
key3 = Button(13)
key4 = Button(19)

key1.when_pressed = handleBtnPress
key2.when_pressed = handleBtnPress
key3.when_pressed = handleBtnPress
key4.when_pressed = handleBtnPress

pause()