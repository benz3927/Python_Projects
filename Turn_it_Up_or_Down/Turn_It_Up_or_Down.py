from cs101audio import *
from random import randint

## load audios

#meh 
beethoven = Audio()
beethoven.open_audio_file("Beethoven.wav")

rach = Audio()
rach.open_audio_file("Rachmaninov.wav")

r2d2 = Audio()
r2d2.open_audio_file("R2 D2 Scream.wav")
r2d2 = r2d2 * 5

violin = Audio()
violin.open_audio_file("Violin.wav")


#exceptional
pirate = Audio()
pirate.open_audio_file("He's a Pirate.wav")

winter = Audio()
winter.open_audio_file("Winter.wav")


TINI = Audio()
TINI.open_audio_file("TINI.wav")

## Organize sounds into meh/not music and truly exceptional music

meh = [beethoven, rach, r2d2,violin]

exceptional = [pirate, winter, TINI]

#  decrease the volume of meh music and increase the volume of truly exceptional music
def main():
    prompt = input("This is a normal radio station. Do you want to listen to no music (none), meh/not music (x), or truly exceptional music (z)")
    if prompt == ('none'):
        print('k bye')
        
    # the loop for trash music -> crank it down
    # from the list of song titles we made, based on an index, we would randommly select a song from index 0 to 2
    
    if prompt == ('x'):
        ran_num = randint(0, 3)
        meh_song=meh[ran_num]
        print("Yikes, a meh song?? How could you??!!")
        
        print("let me turn it down for you.")
    # starting volume for bad songs is higher so there's a need for the program to turn it down
        seconds = len(meh_song)//1000
        volume = 28
        new_song = Audio()
    # loop for decreasing volume
    
        for second in range(0,seconds):
            chunk = meh_song[second* 1000: 1000 * second + 1000]
            volume = volume - 3
            chunk.apply_gain(volume)
            new_song += chunk
        new_song.play()
        if volume < 3:
            print("byebye mid song. Great we have canceled that atrocity!")
        
    # the loop for exceptional music -> crank it up!
    if prompt == ('z'):
        ran_num = randint(0, 2)
        exceptional_song=exceptional[ran_num]
        print("Great song choice, I approve!")
        
        print("let me turn it up for you! :)")
        seconds = len(exceptional_song)//1000
        volume = 0
        new_song = Audio()
    # loop for increasing volume of a song that sounds good, until it breaks our eardrums-- then it would be appropriate to stop
    
        for second in range(0,seconds):
            chunk = exceptional_song[second* 1000: 1000 * second + 1000]
            volume = volume + 0.8
            chunk.apply_gain(volume)
            new_song += chunk
            if second > 20:
                break
        # it starts getting loud at 20 seconds so break helps us stop this part of the loop, move on so that we don't damage our eardrums even more

        new_song.play()
        print("ok, that's nice but it's damaging my eardrums!!!")
        
    print("Ok, thanks for listening to the wack podcast. I hope I was really able to shape and inspire your music tastes!")
    
    # Have fun and enjoy!
            
main()



