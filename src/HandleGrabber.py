import re
from collections import namedtuple

import win32gui

WindowHandleAndName = namedtuple('WindowHandleAndName', ['name', 'handle'])


class HandleGrabber:
    def __init__(self, windowsNames: list[str]):
        self.windowNamesAndHandles = [WindowHandleAndName(name=x, handle=0) for x in windowsNames]

    def grabHandles(self):
        win32gui.EnumWindows(self._enumWindowCallback, '*')
        return self.windowNamesAndHandles

    def _enumWindowCallback(self, handle):
        windowFullName = win32gui.GetWindowText(handle)
        window = next((x for x in self.windowNamesAndHandles if
                       re.match(f'.*{x.name}.*', windowFullName)), None)
        if window: window.handle = handle
