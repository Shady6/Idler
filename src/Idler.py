import os
from typing import List

import keyboard

from src.HandleGrabber import HandleGrabber
from src.Logger import Logger
from src.WindowDto import WindowDto
from src.WindowFocuser import WindowFocuser


class Idler:
    def __init__(self, windows: List[WindowDto]):
        self.windows = windows

        handleGrabber = HandleGrabber([x.windowName for x in self.windows])
        self.windowHandlesAndNames = handleGrabber.grabHandles()
        self.windowFocuser = WindowFocuser([x.handle for x in self.windowHandlesAndNames])

    def idle(self):
        self.listenForExit()
        while True:
            for i in range(len(self.windows)):
                selectedWindowHandle = self.windowFocuser.selectNextWindow()
                selectedWindow = self._getWindowByHandle(selectedWindowHandle)
                self.windowFocuser.focusSelectedWindow()
                Logger.Log(f'Focused window:\t{selectedWindow.windowName}')

                Logger.Log(f'Starting algo manager for window:\t{selectedWindow.windowName}')
                selectedWindow.algoManager.runAlgorithms()

    def _getWindowByHandle(self, handle):
        selectedWindowName = next(x for x in self.windowHandlesAndNames if x.handle == handle)
        selectedWindow = next(x for x in self.windows if x.windowName == selectedWindowName.name)
        return selectedWindow

    def listenForExit(self):
        def callback(event):
            if event.name == 'esc':
                Logger.Log('Will exit')
                os._exit(1)

        keyboard.hook(callback=callback)
