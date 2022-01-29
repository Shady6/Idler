import random

import pyautogui as pag

from src.Logger import Logger


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
            Logger.Log(f'Starting lapse:\t{i}')
            for algo in self.algorithms:
                Logger.Log(f'Starting algorithm:\t{type(algo).__name__}')
                algo.execute()
            lapseInterval = random.randint(self.lapseMinInterval, self.lapseMaxInterval)
            Logger.Log(f'Sleeping for:\t{lapseInterval}\n')
            pag.sleep(lapseInterval)
