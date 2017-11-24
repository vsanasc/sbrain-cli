# SBrain Cli
> Tools to reach high brain efficiency. Your second mind.



## Requirements

* Python (2.7, 3.4, 3.5, 3.6)
* FFmpeg (3.4)

## Install FFmpeg

FFmpeg is the multimedia framework and indispensable for correct operation of this application. 

###OS X

```sh
brew install ffmpeg

```

###Ubuntu 14.04
```sh
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg gstreamer0.10-ffmpeg

```

###Ubuntu 15.04
```sh
sudo apt-get install ffmpeg

```


###Windows

```sh
C:\> choco install ffmpeg

```


For more information and download in your operational system [click here](https://www.ffmpeg.org).


## Installation


```sh
pip install sbrain-cli
```


## How to use

Create a file with a text in english language. And run the follow commad.

```sh
sbrain-cli -f <file-name>
```


## Meta

Felipe Loyola – [@felipel77](https://twitter.com/felipel77) – felipel77@gmail.com

Vitor Santos – [@vsanasc](https://twitter.com/vsanasc) – vsantos.nasc@gmail.com

Distributed under the BSD license. See ``LICENSE`` for more information.


## Contributing

1. Fork it (<https://github.com/vsanasc/sbrain/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request