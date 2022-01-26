from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener


def on_press(key):
    print(f'Key press: {key}')

    if key == Key.esc:
        keyboard_listener.stop()
        mouse_listener.stop()
        exit(0)


def on_click(x, y, button, pressed):
    print(f'Click: ({x},{y}), {button}, {pressed}')


keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_click=on_click)


keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
