import logging


class LogInfo:
    log_file = None

    def __init__(self, log_file):
        self.log_file = log_file
        self.configureLogging(log_file)

    def configureLogging(self, log_file):
        # Log Information
        # set up logging to file - see previous section for more details
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-6s %(levelname)-9s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=log_file,
                            filemode='w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(asctime)s %(name)-7s: %(levelname)-7s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

