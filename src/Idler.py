import pyautogui as pag
from pynput.keyboard import Key, Listener

from src.HandleGrabber import HandleGrabber
from src.WindowDto import WindowDto
from src.WindowFocuser import WindowFocuser


class Idler:
    def __init__(self, windows: list[WindowDto]):
        self.windows = windows
        self.running = False

        handleGrabber = HandleGrabber([x.windowName for x in self.windows])
        self.windowHandlesAndNames = handleGrabber.grabHandles()
        self.windowFocuser = WindowFocuser([x.handle for x in self.windowHandlesAndNames])

    def idle(self):
        listener = self._listenForExit()
        self.running = True

        while self.running:
            for i in range(len(self.windows)):
                selectedWindowHandle = self.windowFocuser.selectNextWindow()
                selectedWindow = self._getWindowByHandle(selectedWindowHandle)

                self.windowFocuser.focusSelectedWindow()
                # Perhaps not needed
                # pag.click(pag.size().width / 2, pag.size().height / 2)
                selectedWindow.algoManager.runAlgorithms()

        listener.stop()

    def _listenForExit(self):
        def on_press(key):
            if key == Key.esc:
                self.running = False

        listener = Listener(on_press=on_press)
        listener.start()
        return listener

    def _getWindowByHandle(self, handle):
        selectedWindowName = next(x for x in self.windowHandlesAndNames if x.handle == handle)
        selectedWindow = next(x for x in self.windows if x.windowName == selectedWindowName)
        return selectedWindow
