from src.AlgoManager import AlgoManager
from src.KeyboardAlgorithm import KeyboardAlgorithm
from src.MouseClickAlgorithm import MouseClickAlgorithm
from src.MouseScrollAlgorithm import MouseScrollAlgorithm
from src.MouseWiggleAlgorithm import MouseWiggleAlgorithm
from src.WindowDto import WindowDto

windows = \
    [
        WindowDto("SkateSpot",
                  AlgoManager(
                      minLapses=5,
                      maxLapses=10,
                      lapseMinInterval=15,
                      lapseMaxInterval=20,
                      algorithms=[
                          KeyboardAlgorithm(
                              charsToWrite='qwertyuiopasdfghjklzxcvbnm,./;[]{}1234567890-=',
                              minWriteSpeed=1,
                              maxWriteSpeed=2,
                              minCharsToWrite=5,
                              maxCharsToWrite=20
                          ),
                          MouseClickAlgorithm(
                              minClicks=5,
                              maxClicks=10,
                              clickMinInterval=1,
                              clickMaxInterval=3
                          ),
                          MouseWiggleAlgorithm(
                              minWiggleTime=10,
                              maxWiggleTime=20,
                          ),
                          MouseScrollAlgorithm()
                      ]
                  )),
        WindowDto("Google Chrome",
                  AlgoManager(
                      minLapses=2,
                      maxLapses=5,
                      lapseMinInterval=10,
                      lapseMaxInterval=20,
                      algorithms=[
                          KeyboardAlgorithm(
                              charsToWrite=['left', 'right', 'up', 'down'],
                              minWriteSpeed=1,
                              maxWriteSpeed=1,
                              minCharsToWrite=6,
                              maxCharsToWrite=10
                          ),
                          MouseWiggleAlgorithm(
                              minWiggleTime=15,
                              maxWiggleTime=30,
                          ),
                          MouseScrollAlgorithm()
                      ]
                  ))
    ]

windowsTest = \
    [
        WindowDto("SkateSpot",
                  AlgoManager(
                      minLapses=1,
                      maxLapses=1,
                      lapseMinInterval=1,
                      lapseMaxInterval=1,
                      algorithms=[
                          MouseWiggleAlgorithm(
                              minWiggleTime=1,
                              maxWiggleTime=1,
                          )
                      ]
                  )),
        WindowDto("Google Chrome",
                  AlgoManager(
                      minLapses=1,
                      maxLapses=1,
                      lapseMinInterval=1,
                      lapseMaxInterval=3,
                      algorithms=[
                          MouseWiggleAlgorithm(
                              minWiggleTime=1,
                              maxWiggleTime=1,
                          )
                      ]
                  )),
    ]
