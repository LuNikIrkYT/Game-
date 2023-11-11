import os
import time
a = input('Напишите D, чтобы продолжить ')
time.sleep(1.5)

if a == 'D':
    print('Загрузка...')
    time.sleep(5)
    os.startfile("video.mp4")
