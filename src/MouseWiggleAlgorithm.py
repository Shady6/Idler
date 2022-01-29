import random

import pyautogui as pag

from src.Logger import Logger


class MouseWiggleAlgorithm:

    def __init__(self, minWiggleTime, maxWiggleTime, singleWiggleTime=2):
        self.minWiggleTime = minWiggleTime
        self.maxWiggleTime = maxWiggleTime
        self.singleWiggleTime = singleWiggleTime

    def execute(self):
        wiggleTime = random.randint(self.minWiggleTime, self.maxWiggleTime)
        for i in range(0, wiggleTime, self.singleWiggleTime):
            Logger.Log(f'Wiggling')
            pag.move(
                random.randint(-100, 100),
                random.randint(-100, 100),
                self.singleWiggleTime)
