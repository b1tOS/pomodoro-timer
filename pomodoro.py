from playsound import playsound
import time

secsForWork = 1500
timeout = 300
k = 0

playsound('http://codeskulptor-demos.commondatastorage.googleapis.com/pang/pop.mp3')

while True:
    secsForWork -= 1
    mins = secsForWork//60
    print('\t' + f'{mins:>02}:{secsForWork-mins*60:>02}', end='\r')
    time.sleep(1)

    if secsForWork == 0:
        playsound('http://codeskulptor-demos.commondatastorage.googleapis.com/pang/pop.mp3')

        while timeout != 0:
            timeout -= 1
            mins = timeout//60
            print('\t' + f'{mins:>02}:{timeout-mins*60:>02}', end='\r')
            time.sleep(1)
            
        playsound('http://codeskulptor-demos.commondatastorage.googleapis.com/pang/pop.mp3')
        k += 1
        timeout = 900 if k % 4 == 0 else 300
        secsForWork = 1500
