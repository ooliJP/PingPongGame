# Ping Pong Game
  
## Description:

This is an old-school pixel art game from the days of Dendy and Sega that we used to play with my brother days and nights. Thanks to the built-in Turtle module and the motivation to play our favorite game with my brother once again that made me make this game using Python.

## Demo:
![ezgif com-gif-maker](https://user-images.githubusercontent.com/69134308/201560419-db344236-72ad-4139-b396-83e363f3415d.gif)


### How to use:
 1. Just run the python file and enjoy!
 
  

## Installation

Just download the file called 'pong.py' and run it.

### Note for Windows users:

Sounds of bouncing will not be working on Windows because I wrote this for Mac and it works little bit differently, so if you are using Windows, you should also import module called winsound and replace every codeline that containing this line:

```bash
os.system("afplay bounce_sound.wav&")
```

to this:

```bash
winsound.PlaySound("bounce.wav&", winsound.SND_ASYNC)
```
