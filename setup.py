try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('sbrain/version.py').read())

setup(
    name='sbrain',
    version=__version__,
    author='Vitor Santos do Nascimento',
    author_email='vsantos.nasc@gmail.com',
    url='https://github.com/vsanasc/sbrain',
    packages=['sbrain'],
    scripts=['bin/sbrain-cli', 'bin/sbrain-cli.py'],
    license='MIT',
    description='Creates a video with text and pronunciation',
    long_description=open('README.md').read(),
    install_requires=[
        'gTTS'
    ],
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Multimedia :: Sound/Audio :: Speech'
    ],
)