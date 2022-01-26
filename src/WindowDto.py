from dataclasses import dataclass

from src.AlgoManager import AlgoManager


@dataclass
class WindowDto:
    windowName: str
    algoManager: AlgoManager
