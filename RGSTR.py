from time import sleep
import mysql.connector
from RGSTRLibrary.RGSTRconnect import *
from RGSTRLibrary.RGSTRupdate import *
from RGSTRLibrary.RGSTRsetup import *
import nxppy
import pygame
from gtts import gTTS
pygame.init()
def playsound(status,user):
    if status=="1":
        voice=str("{} signed out".format(str(user)))
    elif status=="0":
        voice=str("{} signed in".format(str(user)))
    else:
        voice=("Error")
    tts=gTTS(text=voice,lang="en")
    tts.save("tts.mp3")
    pygame.mixer.music.load("tts.mp3")
    pygame.mixer.music.play()
        
mifare=nxppy.Mifare()
if __name__ == "__main__":
    configfile="config.ini"
    #Connect to database
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT *\nFROM users")
    except:
        dbsetup(configfile,cursor)
    #Poll for cards
    while True:
        UID=""
        while UID=="":
            try:
                UID=mifare.select()
            except nxppy.SelectError:
                sleep(0.5)
                pass
        try:
            #Search database for cards
            user=databaselookup(UID,configfile)
            status=(chr(user[0][2][0]))
            user=user[0][0]
            print ('status before:',status)
            updatestatus(UID,status,configfile)
            playsound(status,user)
            sleep(0.5)
        except:
            playsound(3,0)
