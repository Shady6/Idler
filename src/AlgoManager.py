import random

import pyautogui as pag


class AlgoManager:

    def __init__(self, minLapses, maxLapses, lapseMinInterval, lapseMaxInterval, algorithms):
        self.algorithms = algorithms
        self.lapseMinInterval = lapseMinInterval
        self.lapseMaxInterval = lapseMaxInterval
        self.maxLapses = maxLapses
        self.minLapses = minLapses

    def runAlgorithms(self):
        lapses = random.randint(self.minLapses, self.maxLapses)
        for i in range(lapses):
            for algo in self.algorithms:
                algo.execute()
            lapseInterval = random.randint(self.lapseMinInterval, self.lapseMaxInterval)
            pag.sleep(lapseInterval)
