from gpiozero import Button
from signal import pause

def say_hello(button_number):
    print("Button: " + str(button_number))

key1 = Button(5)
key2 = Button(6)
key3 = Button(13)
key4 = Button(19)

key1.when_pressed = say_hello(1)
key2.when_pressed = say_hello(6)
key3.when_pressed = say_hello(13)
key4.when_pressed = say_hello(19)

pause()