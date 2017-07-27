import unicornshield as unicorn
import time
unicorn.brightness(0.5)
while True:

    #rosa
    for x in range(9):
        unicorn.setPixel(x,0,255,115)
        unicorn.show()
        time.sleep(0.15)
    for x in range(9):
        unicorn.setPixel(x,0,0,0)
        unicorn.show()
        time.sleep(0.05)

    unicorn.setAll(255,0,0)
    time.sleep(0.5)
    unicorn.show()

    unicorn.setAll(0,0,0)
    time.sleep(0.3)
    unicorn.show()

    unicorn.setAll(255,0,0)
    time.sleep(0.5)
    unicorn.show()

    unicorn.setAll(0,0,0)
    time.sleep(0.3)
    unicorn.show()

    time.sleep(3)
