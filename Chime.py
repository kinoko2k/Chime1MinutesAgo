from mutagen.mp3 import MP3 as mp3
import pygame
import time

filename = 'chime-1min.mp3'
interval_time = 60

interval_time = int(input("アラーム間隔を秒数で設定せよ >>"))
print("==================================================")
print("開始しました")
print("60秒後になるとchime-1min.mp3が鳴ります。")
print("このプログラムを終了するには、ctrl+cを押してください。")
print("==================================================")

pygame.mixer.init()
pygame.mixer.music.load(filename)


while True:
    pygame.mixer.music.play()
    time.sleep(interval_time)
    print(interval_time)

pygame.quit()
