import logging

class Logger:
    isDebug = True
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%I:%M:%S')

    @staticmethod
    def Log(msg):
        if Logger.isDebug:
            logging.info(msg)
