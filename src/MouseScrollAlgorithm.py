import random

import pyautogui as pag


class MouseScrollAlgorithm:

    def __init__(self, minScrollValue=-10, maxScrollValue=10):
        self.maxScrollValue = maxScrollValue
        self.minScrollValue = minScrollValue

    def execute(self):
        scrollValue = random.randint(self.minScrollValue, self.maxScrollValue)
        pag.scroll(scrollValue)
        pag.scroll(-scrollValue)
