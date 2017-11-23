#!python
# -*- encoding: utf-8 -*-


from __future__ import print_function
from sbrain import __version__
from gtts import gTTS
from os import *

import sys
import argparse
import codecs
import re
import subprocess
import shutil
import os
# Args
desc = "Creates a video with text and pronunciation ({v})".format(v=__version__)
parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)

text_group = parser.add_mutually_exclusive_group(required=True)  
text_group.add_argument('-f', '--file', help="file text")

parser.add_argument('--debug', action="store_true")

args = parser.parse_args()



try:
    if args.file:


        with codecs.open(args.file, 'r', 'utf-8') as ft:
            text = ft.read()

        delimiters = '.', '...', '?', '!'
        regexPattern = '|'.join(map(re.escape, delimiters))
        lista = re.split(regexPattern, text.replace('\n',''))
        
        concat = 'concat:'


        if not os.path.exists('temp'):
            os.makedirs('temp')

        for idx, val in enumerate(lista):

            nameFile = 'temp/'+ str(idx)+'.mp3'
            tts = gTTS(text=val, lang='en')
            tts.save(nameFile)

            if idx > 0:
                concat += '|'

            concat += nameFile


        #ffmpeg -i 'concat:input1|input2' -codec copy output
        subprocess.call(['ffmpeg','-i', concat, '-codec', 'copy','output.mp3'])

        if os.path.exists('temp'):
            shutil.rmtree('temp')



    
except Exception as e:
    print("ERROR: ", e, file=sys.stderr)