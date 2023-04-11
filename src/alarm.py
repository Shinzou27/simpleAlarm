import time
from playsound import playsound

timeString = input('Insira um horário para despertar. (Formato = 00:00)\n')
def setAlarm():
    if(time.strftime('%H:%M') == timeString):
        playsound('sound.mp3')
    else:
        time.sleep(1)
        setAlarm()
    
setAlarm()