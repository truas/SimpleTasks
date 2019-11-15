import argparse
import distutils.util as util


class CommandLineSimpletools:
    input_folder = None
    output_folder = None
    overlap_folder = None
    match_flag = None
    randomize = None
    log_file = None

    def __init__(self):
        """
        Arguments for command line - standard input and output
        constructor
        """
        parser = self.command_line_parameters()
        args = parser.parse_args()
        self.input_folder = args.inf
        self.output_folder = args.ouf
        self.overlap_folder = args.ovp
        self.match_flag = args.match
        self.randomize = args.rdz
        self.log_file = args.lgf

    def command_line_parameters(self):
        parser = argparse.ArgumentParser(description="Default command line for standard input and output")
        parser.add_argument('--input', '-i', type=str, action='store', dest='inf', metavar='<path>',
                            required=True,
                            help='Input folder')
        parser.add_argument('--output', '-o', type=str, action='store', dest='ouf', metavar='<path>',
                            required=True,
                            help='Output folder')
        parser.add_argument('--overlap', '-p', type=str, action='store', dest='ovp', metavar='<path>',
                            required=False,
                            help='Folder to overlap files from input folder')
        parser.add_argument('--match', '-m', type=util.strtobool, action='store', dest='match', metavar='<parameter>',
                            required=False, default=True,
                            help='[optional] [True] (Default) - Will match files from --input to --overlap and '
                                 'copy files from --overlap to --output.'
                                 '[False] - Will match files from --input and --overlap and copy both to --output',
                            choices=[True, False])
        parser.add_argument('--randomize', '-r', type=int, action='store', dest='rdz', metavar='<value>',
                            required=False, default=10,
                            help='Number of random files to select. Has to be smaller or equal the number of files.')
        parser.add_argument('--logging', '-l', type=str, action='store', dest='lgf', metavar='<path>',
                            required=False, default='info.log',
                            help='Log path specification')
        return parser
    # parameter list for command line
