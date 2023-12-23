from pynput.mouse import Listener

import os

global counter
counter = 0


def on_click(x, y, button, pressed):
    if pressed:
        os.system("cls")
        global counter
        counter += 1
        print(f"Mouse clicked: {counter}")


with Listener(on_click=on_click) as listener:
    listener.join()
