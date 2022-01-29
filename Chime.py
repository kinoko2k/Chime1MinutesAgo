from mutagen.mp3 import MP3 as mp3
import pygame
import time

filename = 'chime-1min.mp3'
interval_time = 0 # 再生間隔を秒数で指定する

interval_time = int(input("アラーム間隔を秒数で設定してください。"))
print("==================================================")
print("開始しました")
print("設定した秒数になるとchime-1min.mp3が鳴ります。")
print("このプログラムを終了するには、ctrl+cを押してください。")
print("==================================================")

pygame.mixer.init()
pygame.mixer.music.load(filename)


while True:
    pygame.mixer.music.play()
    time.sleep(interval_time)
    print(interval_time)

pygame.quit()
