
from gtts import gTTS
#from google.cloud import translate
#from mutagen.mp3 import MP3

from .FFmpeg import FFCommandGenerator


import shutil
import os
import sys
import subprocess
import codecs
import re
import random
import urllib2
import urllib
import json

class Builder():

    def __init__(self):
        # Configs
        self.delimiters = '\n' # '.', '...', '?', '!', 
        self.random = False
        self.output = 'output.mp3'
        self.file = None
        self.language = 'en'
        self.translate = None
        self.translation_repeat = 5
        self.repeat = 1
        self.time = True
        self.api_key_google = ''

        
        # initializers
        self.ffmpeg = FFCommandGenerator()
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.temp_session_dir = '{}/temp-session'.format(self.base_dir)
        self.temp_final_dir = '{}/phrases/'.format(self.base_dir)
        self.phrases = []
        self.files = []

    def generate_audio(self):

        if os.path.exists(self.temp_session_dir):
            shutil.rmtree(self.temp_session_dir)

        if os.path.exists(self.temp_final_dir):
            raise ValueError('Already phrases folder')
            sys.exit(1)

        os.makedirs(self.temp_session_dir)
        os.makedirs(self.temp_final_dir)


        self._get_phrases_from_file(self.file)
        #print(json.dumps(self.phrases))
        #sys.exit(1)
        self._get_audios_from_google()


        self.ffmpeg.add_concat_files(self.files)
        command = self.ffmpeg.final(self.output)


        os.system(command)

        if os.path.exists(self.temp_session_dir):
            shutil.rmtree(self.temp_session_dir)
        

    def _get_audios_from_google(self):
        for idx, val in enumerate(self.phrases):
            self._generate_session_phrase(idx, val)


    def _generate_session_phrase(self, index, phrase):

        session_files = []

        phraseFile = '{}/{}.mp3'.format(self.temp_final_dir, index)

        originalFile = '{}/temp-session/original-{}.mp3'.format(self.base_dir, index)
        tts = gTTS(text=phrase, lang=self.language)
        tts.save(originalFile)

        if self.translate:
            translateFile = '{}/temp-session/translate-{}.mp3'.format(self.base_dir, index)
            
            translateText = self._get_translate(text=phrase, source=self.language, target=self.translate)

            tts = gTTS(text=translateText, lang=self.translate)
            tts.save(translateFile) 

            for x in range(self.translation_repeat):
                session_files.append(translateFile)
                session_files.append('{}/2s.mp3'.format(self.base_dir))

        for x in range(self.repeat):
            session_files.append(originalFile)
            session_files.append('{}/4s.mp3'.format(self.base_dir))


        ffmpeg_session = FFCommandGenerator()
        ffmpeg_session.add_concat_files(session_files)
        command = ffmpeg_session.final(phraseFile)
        
        os.system(command)

        self.files.append(phraseFile)




    def _get_phrases_from_file(self, file):

        with codecs.open(file, 'r', 'utf-8') as ft:
            text = ft.read()

        regexPattern = '|'.join(map(re.escape, self.delimiters))
        listPhrases = re.split(regexPattern, text.replace('||','|'))

        #if random:
        #    listPhrases = random.choice(listPhrases)
        
        for p in listPhrases:
            if p != '' and p != ' ':
                self.phrases.append(p)


    def _get_translate(self, text, source, target):

        url = 'https://www.googleapis.com/language/translate/v2?q={}&source={}&target={}&key={}'.format(urllib.quote(text.encode('utf8')), source,target, self.api_key_google)
        
        print(url)

        response = urllib2.urlopen(url).read()
        data = json.loads(response)

        return data["data"]["translations"][0]["translatedText"]




