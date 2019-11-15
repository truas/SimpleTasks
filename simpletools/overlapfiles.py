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

    logfile = params.log_file
    logs = LogInfo(logfile)  # Log  configuration

    source_path = os.path.join(ppydir_name, params.input_folder)
    dest_path = os.path.join(ppydir_name, params.output_folder)
    overlap_path = os.path.join(ppydir_name, params.overlap_folder)
    match_flag = params.match_flag

    filenames_input = os.listdir(source_path)
    filenames_overlap = os.listdir(overlap_path)


    try:
        if match_flag:
            filemanip.fileMatching(filenames_input, filenames_overlap, dest_path, overlap_path)
        else:
            filemanip.fileMatchingValidation(filenames_input, filenames_overlap, source_path, dest_path, overlap_path)
    except:
        logging.error('Could not copy files.')

    logging.info('Program finished.')


