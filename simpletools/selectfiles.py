import random
import logging
import os
import sys

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# self-packages
from simpletools.commandlinesimpletools import CommandLineSimpletools
from simpletools.filemanip import FileManipulation
from simpletools.loginfo import LogInfo

if __name__ == "__main__":
    filemanip = FileManipulation()
    params = CommandLineSimpletools()

    source_path = os.path.join(ppydir_name, params.input_folder)
    dest_path = os.path.join(ppydir_name, params.output_folder)
    random_files = params.randomize
    logfile = params.log_file

    logs = LogInfo(logfile)
    filenames = random.sample(os.listdir(source_path), random_files)
    filemanip.randonFileSelection(filenames, source_path, dest_path)

    logging.info('Program finished with no errors')
