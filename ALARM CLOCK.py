# Python Alarm Clock

import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file =  "sound.mp3"
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}",end="\r")
        time.sleep(1)   
        if current_time == alarm_time:
            print("Alarm ringing!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False  #WIILL SET BACK IT TO START
       
            
            

            is_running = False
            
       
alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
set_alarm(alarm_time)
    
    
