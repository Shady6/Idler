import random
import win32gui

class WindowFocuser:
    def __init__(self, windowsHandles: list[int]):
        self.windowsHandles = windowsHandles
        self.pickedWindows = []

    def selectNextWindow(self):
        if len(self.pickedWindows) == len(self.windowsHandles):
            self._reset()

        randomWindowHandle = random.choice(self.windowsHandles)
        while randomWindowHandle in self.pickedWindows:
            randomWindowHandle = random.choice(self.windowsHandles)
        self.pickedWindows.append(randomWindowHandle)
        return randomWindowHandle

    def focusSelectedWindow(self):
        win32gui.SetForegroundWindow(self.pickedWindows[-1])

    def _reset(self):
        self.pickedWindows = []
