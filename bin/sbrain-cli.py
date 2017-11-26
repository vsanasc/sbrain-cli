#!python
# -*- encoding: utf-8 -*-


from __future__ import print_function
from sbrain import __version__
from sbrain.engine import Builder
from os import *


import sys
import argparse
import os
# Args
desc = "Creates a video with text and pronunciation ({v})".format(v=__version__)
parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)

#text_group = parser.add_mutually_exclusive_group(required=True)  

parser.add_argument('-f', '--file', help="file text")
parser.add_argument('-l', '--language', help="language text")
parser.add_argument('-t', '--translate', help="translate")
parser.add_argument('-tr', '--translation-repeat', help="repeat translate")
parser.add_argument('-r', '--repeat', help="repeat language")
parser.add_argument('-key', '--api_key', help="api key google")
parser.add_argument('--no-time',  help="time")
parser.add_argument('-o', '--output', help="output file")

parser.add_argument('--debug', action="store_true")
parser.add_argument('--random', help='Disable random generator')


if len(sys.argv) == 1:
	parser.print_help()
	sys.exit(1)

args = parser.parse_args()

b = Builder()

try:

	if args.file:
		b.file = args.file

	if args.language:
		b.language = args.language

	if args.translate:
		b.translate = args.translate

	if args.translation_repeat:
		b.translation_repeat = int(args.translation_repeat)

	if args.api_key:
		b.api_key_google = args.api_key

	if args.repeat:
		b.repeat = int(args.repeat)

	if args.no_time:
		b.time = False

	if args.output:
		b.output = args.output

	if args.random:
		b.random = True


	
	b.generate_audio()

    
except Exception as e:

    print("ERROR: ", e, file=sys.stderr)