import unicornshield as unicorn
import time

while True:
    if unicorn.nose() > 0.3:
        unicorn.leftEyeOn()
        unicorn.rightEyeOn()
        for x in range(9):
            unicorn.setPixel(x,255,0,255)
            unicorn.show()
            time.sleep(0.2)
        time.sleep(2)
        unicorn.clear()
        unicorn.leftEyeOff()
        unicorn.rightEyeOff()
