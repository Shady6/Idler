import getopt
import sys

from src.Idler import Idler
from src.Logger import Logger
from src.WindowPresets import windows

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'd')
    Logger.isDebug = True if '-d' in [x[0] for x in opts] else False

    idler = Idler(windows=windows)
    idler.idle()