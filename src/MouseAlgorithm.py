import random

import pyautogui as pag


class MouseAlgorithm:

    def __init__(self, minClicks, maxClicks, clickMinInterval, clickMaxInterval):
        self.minClicks = minClicks
        self.maxClicks = maxClicks
        self.clickMinInterval = clickMinInterval
        self.clickMaxInterval = clickMaxInterval

    def execute(self):
        clicksNumber = random.randint(self.minClicks, self.maxClicks)
        for i in range(clicksNumber):
            clickInterval = random.randint(self.clickMinInterval, self.clickMaxInterval)
            pag.sleep(clickInterval)
            pag.click(pag.size().width / 2, pag.size().height / 2)
