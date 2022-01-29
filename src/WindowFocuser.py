import random
from typing import List

import win32gui

from src.Logger import Logger


class WindowFocuser:
    def __init__(self, windowsHandles: List[int]):
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
        Logger.Log(f'Will pick window {self.pickedWindows[-1]}')
        win32gui.SetForegroundWindow(self.pickedWindows[-1])

    def _reset(self):
        self.pickedWindows = []
