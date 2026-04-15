from pynput.keyboard import Key, Controller
import time
keyboard = Controller()


class song(object):
    def __init__(self, key, seconds):
        self.key = key
        self.seconds = seconds

    def songs(self):
        return keyboard.press(self.key), time.sleep(self.seconds)
#       keyboard.release(key)
#       time.sleep(seconds)

