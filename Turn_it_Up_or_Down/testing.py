from cs101audio import *
from random import randint

## load audios

#meh 
pirate = Audio()
pirate.open_audio_file("He's a Pirate.wav")
volume = 0
print(len(pirate))