import getopt
import sys

from src.AlgoManager import AlgoManager
from src.Idler import Idler
from src.Logger import Logger
from src.MouseWiggleAlgorithm import MouseWiggleAlgorithm
from src.WindowDto import WindowDto

# windows = \
#     [
#         WindowDto("SkateSpot",
#                   AlgoManager(
#                       minLapses=1,
#                       maxLapses=2,
#                       lapseMinInterval=1,
#                       lapseMaxInterval=5,
#                       algorithms=[
#                           KeyboardAlgorithm(
#                               charsToWrite='qwertyuiop',
#                               minWriteSpeed=1,
#                               maxWriteSpeed=5,
#                               minCharsToWrite=2,
#                               maxCharsToWrite=4
#                           ),
#                           MouseClickAlgorithm(
#                               minClicks=2,
#                               maxClicks=3,
#                               clickMinInterval=1,
#                               clickMaxInterval=2
#                           ),
#                           MouseWiggleAlgorithm(
#                               minWiggleTime=4,
#                               maxWiggleTime=6,
#                           ),
#                           MouseScrollAlgorithm()
#                       ]
#                   ))
#     ]

windows = \
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

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'd')
    Logger.isDebug = True if '-d' in [x[0] for x in opts] else False

    idler = Idler(windows=windows)
    idler.idle()
