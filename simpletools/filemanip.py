import os
import shutil
import logging

from simpletools.loginfo import LogInfo


class FileManipulation:
    def __init__(self):
        """
        constructor
        """

    def randonFileSelection(self, filenames, input_folder, output_folder):
        """Copy files from one folder to another"""
        for fname in filenames:
            srcpath = os.path.join(input_folder, fname)
            shutil.copy(srcpath, output_folder)  # copy file


    def fileMatching(self, filenames, overlapfiles, dest_path, overlap_path):
        """copy files from one folder to another when there is a match the -en.txt, -es.txt ... """
        for fname in filenames:
            tmp_achor = fname.split('.')
            for overlapfile in overlapfiles:
                tmp_moveable = overlapfile.split('.')
                if tmp_achor[0][:-3] == tmp_moveable[0][:-3]: # we are mapping the language right next to the extension
                    srcpath = os.path.join(overlap_path, overlapfile)
                    shutil.copy(srcpath, dest_path)  # extract file
                else:
                    logging.warning('No --overlap files matched')

    def fileMatchingValidation(self, filenames, overlapfiles, source_path, dest_path, overlap_path):
        """copy files from one folder to another when there is a match the -en.txt, -es.txt ... """
        for fname in filenames:
            tmp_achor = fname.split('.')
            for overlapfname in overlapfiles:
                tmp_moveable = overlapfname.split('.')
                if tmp_achor[0][:-3] == tmp_moveable[0][:-3]:  # we are mapping the regex right next to the extension
                    srcpath_a = os.path.join(overlap_path, overlapfname)
                    srcpath_b = os.path.join(source_path, fname)
                    shutil.copy(srcpath_a, dest_path)
                    shutil.copy(srcpath_b, dest_path)
                else:
                    logging.warning('No files moved from --input and --overlap')
                    pass