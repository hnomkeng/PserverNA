import time
def SLEEPDELAY(Tdelay):
    hourX = int(time.strftime("%H"))
    secondsX  = int(time.strftime("%S"))
    minuteX = int(time.strftime("%M"))
    craftsecond = secondsX + (minuteX*60) + (hourX*60)
    if (craftsecond > Tdelay):
        return 0
    elif (craftsecond < Tdelay):
        send_delay = (Tdelay - craftsecond)
        return int(send_delay)
    else:
        return 0

#set time delay
def SETDELAY(Tdelay):
    hourX = int(time.strftime("%H"))
    secondsX  = int(time.strftime("%S"))
    minuteX = int(time.strftime("%M"))
    craftsecond = secondsX + Tdelay + (minuteX*60) + (hourX*60)
    return int(craftsecond)
