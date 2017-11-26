

class FFCommandGenerator():

    def __init__(self):
        self.command = ['ffmpeg']


    def add_concat_files(self, files):
        self.command.append('-i')

        concat = "'concat:"

        for (idx, f) in enumerate(files):
            
            if idx > 0:
                concat += '|'

            concat += f

        concat += "'"
        self.command.append(concat)
        self.command.append('-c:v')
        self.command.append('-c:a')


    def final(self, output='output.mp3'):

        self.command.append(output)
        return ' '.join(self.command)

