import random

import pyautogui as pag

from src.Logger import Logger


class KeyboardAlgorithm:

    def __init__(self, charsToWrite, minCharsToWrite, maxCharsToWrite, minWriteSpeed, maxWriteSpeed):
        self.charsToWrite = charsToWrite
        self.minCharsToWrite = minCharsToWrite
        self.maxCharsToWrite = maxCharsToWrite
        self.minWriteSpeed = minWriteSpeed
        self.maxWriteSpeed = maxWriteSpeed

    def execute(self):
        writeSpeed = random.randint(self.minWriteSpeed, self.maxWriteSpeed)
        numberOfCharsToWrite = random.randint(
            self.minCharsToWrite, self.maxCharsToWrite)

        randomCharsToWrite = [random.choice(self.charsToWrite) for _ in range(numberOfCharsToWrite)]
        writeInterval = 1 / writeSpeed

        for randomChar in randomCharsToWrite:
            pag.write(randomChar, interval=writeInterval) if len(randomChar) == 1 \
                else pag.press(randomChar, interval=writeInterval)
            Logger.Log(f'Wrote:\t{randomChar}')
