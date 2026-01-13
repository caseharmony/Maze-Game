
def hour(time):
    hrs=int(time[:-6])
    hrs=hrs + 1
    hrs=str(hrs)
    if len(hrs)==1:
        hrs='0'+hrs
    time=hrs+time[-6:]
    return time

def minute(time):
    mins=int(time[-5:-3])
    mins=mins + 1
    if mins==60:
        mins=0
        time=hour(time)
    mins=str(mins)
    if len(mins)==1:
        mins='0'+mins
    time=time[:-5]+mins+time[-3:]
    return time

def second(time):
    sec=int(time[-2:])
    sec=sec + 1
    if sec==60:
        sec=0
        time=minute(time)
    sec=str(sec)
    if len(sec)==1:
        sec='0'+sec
    time=time[:-2]+sec
    return time

time='00:00:00'
while True:
        time=second(time)
        print(time)