from guizero import *
from pygame import mixer
from pathlib import Path
from tinytag import *
from io import BytesIO
from PIL import *
from PIL import Image


# import re

# from get_cover_art import *

# import audio_metadata
# from tkinter import *
#
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3
# from PIL import Image
# from mutagen import File

#tinytag






def main():
    # song2 = None
    song2 = ''

    mixer.init()



    def get_file():
        # file_name.value = app.select_file()
        #file_name.value = app.select_file(filetypes=[["Mp3 files", "*.mp3"]])
        global song2
        song2 = app.select_file(filetypes=[["Mp3 files", "*.mp3"]])
        show_info(song2)
        mixer.music.load(song2)
        song_name = Path(song2).stem
        song_name2 = Path(song2)
        print(song_name2)

        file_name.value = "Currently Song is playing : \n" + song_name




    def show_info(song):
        tag = TinyTag.get(song, image=True)
        lbx_track_info.clear()
        lbx_track_info.append(f'Artist: {tag.artist}')
        lbx_track_info.append(f'Title: {tag.title}')
        lbx_track_info.append(f'Album: {tag.album}')
        lbx_track_info.append(f'Length: {tag.duration / 60:.1f} minutes')
        lbx_track_info.append(f'Released: {tag.year}')

        # image_data = tag.get_image()
        # pic_art.image = Image.open(BytesIO(image_data))


        try:
            image_data = tag.get_image()
            pic_art.image = Image.open(BytesIO(image_data))
        except UnidentifiedImageError:
            pic_art.image = 'blank.png'

    def play_song():
        mixer.music.play()
        song_status.value = "Song is playing"
     # playsound(song)

    def pause_song():
        mixer.music.pause()
        song_status.value = "Song is paused"


    def resume_song():
        # if not mixer.music.pause:
        #     song_status.value = "After resuming, It is playing"
        #
        # else:
        mixer.music.unpause()
        song_status.value = "After resuming, It is playing"



    def stop_song():
        mixer.music.stop()
        song_status.value = "Song is stopped"



    app = App(title="Mp3 Player", width=600, height=300, bg="grey")
    window1 = Window(app, title='Order Preview', width=450, height=600)
    lbx_track_info = ListBox(window1, width=400, height=250, scrollbar=True)
    # Box for space
    Box(window1, width=380, height=10)
    pic_art = Picture(window1, width=300, height=250)

    box_1 = Box(app, width=400, height=200, align="bottom")

    # song = app.select_file(filetypes=[["Mp3 files", "*.mp3"]])
    # song_name= Path(song).stem



    PushButton(app, command=get_file, text="Get file")

    # song_status = Text(app,color="black")
    play = PushButton(box_1, text="Play Song", align="left", command=play_song) #, padx=50)
    play.bg = "green"

    pause = PushButton(box_1, text="Pause Song", align="left", command=pause_song)
    pause.bg = "red"

    resume = PushButton(box_1, text="Resume Song", align="left", command=resume_song)
    resume.bg = "orange"
    stop = PushButton(box_1, text="Stop Song", command=stop_song, align="left")# image="stop.png", height=50, width=80)
    stop.bg = "blue"


    song_status = Text(app, color="black")

    file_name = Text(app,color="white")
    #
    # file_name2 = Text(box_1,color="white")
    # file_name2.value = song2
    # print(song2)
    # get_file
    # file_name2.value = get_file.song2
    # mixer.music.load(get_file.song2)
    # # print(song2)


    app.display()


main()
