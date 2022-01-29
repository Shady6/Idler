import random

import pyautogui as pag

from src.Logger import Logger


class MouseClickAlgorithm:

    def __init__(self, minClicks, maxClicks, clickMinInterval, clickMaxInterval):
        self.minClicks = minClicks
        self.maxClicks = maxClicks
        self.clickMinInterval = clickMinInterval
        self.clickMaxInterval = clickMaxInterval

    def execute(self):
        clicksNumber = random.randint(self.minClicks, self.maxClicks)
        for i in range(clicksNumber):
            pag.click(pag.size().width / 2, pag.size().height / 2)
            Logger.Log('Clicked')
            clickInterval = random.randint(self.clickMinInterval, self.clickMaxInterval)
            pag.sleep(clickInterval)


