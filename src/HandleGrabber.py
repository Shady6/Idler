import re
from dataclasses import dataclass
from typing import List

import win32gui


@dataclass
class WindowHandleAndName:
    name: str
    handle: int


class HandleGrabber:
    def __init__(self, windowsNames: List[str]):
        self.windowNamesAndHandles = [WindowHandleAndName(name=x, handle=0) for x in windowsNames]

    def grabHandles(self):
        win32gui.EnumWindows(lambda handle, _: self._enumWindowCallback(handle), '*')
        return self.windowNamesAndHandles

    def _enumWindowCallback(self, handle):
        windowFullName = win32gui.GetWindowText(handle)
        window = next((x for x in self.windowNamesAndHandles if
                       re.match(f'.*{x.name}.*', windowFullName)), None)
        if window:
            window.handle = handle
