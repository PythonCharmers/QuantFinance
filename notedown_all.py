#!/usr/bin/env python
"""
A little script that launches `notedown.py` multiple times to convert multiple
notebooks from Jupyter to Markdown or back.

Copyright (c) 2019 Python Charmers

Requires:
    pip install notedown
"""

import argparse
import logging
import io
import sys
import os.path
import glob
import pathlib
import pkg_resources
import subprocess

try:
    from notedown.main import ftdetect
except ImportError:
    print('This script requires `notedown`. (Try `pip install notedown`.)',
          file=sys.stderr)
    sys.exit(1)


examples = """ 
Example usage of notedown_all
-----------------------------

Convert markdown into notebook:

    notedown_all **/**.md
    # Equivalent to this:
    notedown_all --from markdown --to notebook **/*.md

    # Or:
    notedown_all *.ipynb
    # Equivalent to this:
    notedown_all --from notebook --to markdown *.ipynb


Convert notebooks into markdown, with outputs intact:

    notedown_all input.ipynb [input2.ipynb ...] --from notebook --to markdown


Convert notebooks into markdown, stripping all outputs:

    notedown_all input.ipynb [input2.ipynb ...] --from notebook --to markdown --strip


Strip the output cells from markdown:

    notedown_all with_output_cells.md --to markdown --strip > no_output_cells.md


Convert from markdown and execute:

    notedown_all input.md --run
"""


def command_line_parser():
    """Create parser for command line usage."""
    description = "Convert multiple Jupyter notebooks to/from markdown."
    parser = argparse.ArgumentParser(description=description,
                                     epilog='For example usage, ' +
                                            'run notedown_all --examples.')
    parser.add_argument('input_files', nargs='+',
                        help="markdown input files")
    parser.add_argument('--from',
                        dest='informat',
                        choices=('notebook', 'markdown'),
                        help=("format to convert from, defaults to file extension"))
    parser.add_argument('--to',
                        dest='outformat',
                        choices=('notebook', 'markdown'),
                        help=("format to convert to. Defaults to opposite of the source format. "
                              "Setting --render forces this to 'markdown'"))
    parser.add_argument('--run', '--execute',
                        action='store_true',
                        help=("run the notebook, executing the "
                              "contents of each cell"))
    parser.add_argument('--timeout',
                        default=30,
                        type=int,
                        help=("set the cell execution timeout (in seconds)"))
    parser.add_argument('--strip',
                        action='store_true',
                        dest='strip_outputs',
                        help=("strip output cells"))
    parser.add_argument('--precode',
                        nargs='+',
                        default=[],
                        help=("additional code to place at the start of the "
                              "notebook, e.g. --pre '%%matplotlib inline' "
                              "'import numpy as np'"))
    parser.add_argument('--render',
                        help=('render outputs, forcing markdown output'),
                        action='store_true')
    parser.add_argument('--template',
                        help=('template file'))
    parser.add_argument('--overwrite',
                        default=False,
                        help=('whether or not to overwrite any output files. '
                              'Necessary if the source and target formats are the same.'),
                        action='store_true')
    parser.add_argument('--match',
                        default='strict',
                        help=("determine kind of Markdown code blocks that get "
                              "converted into code cells. "
                              "choose from 'all', 'fenced', "
                              "'strict' (default) or a specific language to match on"))
    parser.add_argument('--output-dir',
                        default='.',
                        help=('save newly created files in the given directory'))
    parser.add_argument('--examples',
                        help=('show example usage'),
                        action='store_true')
    parser.add_argument('--version',
                        help=('print version number'),
                        action='store_true')
    parser.add_argument('--debug',
                        help=('show logging output'),
                        action='store_true')

    return parser


def main(args, help=''):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.version:
        print(__version__)
        sys.exit()

    if args.examples:
        print(examples)
        sys.exit()

    try:
        input_filenames = args.input_files
        informat = args.informat or ftdetect(input_filenames[0])
        outformat = args.outformat or ('notebook' if informat == 'markdown' else 'markdown')
        assert None not in (informat, outformat)
        if not args.overwrite:
            assert informat != outformat
    except:
        # if e.g. no input file
        sys.stdout.write(help)
        sys.exit()

    loop_over_files(input_filenames, informat, outformat, args)


def loop_over_files(filenames, informat, outformat, args):
    output_ext = {'markdown': '.md',
                  'notebook': '.ipynb'}
    insuffix = output_ext[informat]
    outsuffix = output_ext[outformat]
    
    extra_args = []
    if args.run:
        extra_args.append('--run')

    if args.strip_outputs:
        extra_args.append('--strip')

    if args.render:
        extra_args.append('--render')

    for input_filename in filenames:
        path = pathlib.Path(input_filename)
        assert path.suffix.lower() == insuffix
        output_filename = os.path.join(args.output_dir, path.stem + outsuffix)
        logging.debug(f'Converting {input_filename} to {output_filename}')

        input_file = io.open(path, 'r', encoding='utf-8')
        if not args.overwrite and os.path.exists(output_filename):
                sys.stdout.write(f'The file {output_filename} exists but '
                                 f'--overwrite was not specified. Aborting.')
                sys.exit()
        with open(output_filename, mode='wb') as f:
            notedown_args = ['notedown', path,
                             '--from', informat,
                             '--to', outformat,
                             '--match=strict'] + extra_args
            subprocess.call(notedown_args, stdout=f)


def app():
    parser = command_line_parser()
    args = parser.parse_args()
    main(args, help=parser.format_help())


if __name__ == '__main__':
    app()
