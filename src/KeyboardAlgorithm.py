import random

import pyautogui as pag


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
        charsToWrite = ''.join([self.charsToWrite[random.randint(
            0, len(self.charsToWrite) - 1)] for _ in range(numberOfCharsToWrite)])
        pag.write(message=charsToWrite, interval=1 / writeSpeed)
