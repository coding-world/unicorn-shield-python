import unicornshield as unicorn
import time
unicorn.brightness(0.5)
while True:
    #rot
    unicorn.setPixel(0,155,0,0)
    unicorn.setPixel(1,155,0,0)
    unicorn.show()
    time.sleep(0.2)
    #gelb
    unicorn.setPixel(2,255,200,0)
    unicorn.setPixel(3,255,200,0)
    unicorn.show()
    time.sleep(0.2)
    #green
    unicorn.setPixel(4,0,255,0)
    unicorn.setPixel(5,0,255,0)
    unicorn.show()
    time.sleep(0.2)
    #jp-green
    unicorn.setPixel(6,0,255,115)
    unicorn.setPixel(7,0,255,115)
    unicorn.setPixel(8,0,255,115)
    unicorn.show()
    time.sleep(0.3)

    #rosa
    for x in range(9):
        unicorn.setPixel(x,155,0,155)
        unicorn.show()
        time.sleep(0.15)
    for x in range(9):
        unicorn.setPixel(x,0,0,0)
        unicorn.show()
        time.sleep(0.05)

    unicorn.setAll(155,0,0)
    time.sleep(0.3)
    unicorn.show()

    unicorn.setAll(255,200,0)
    time.sleep(0.3)
    unicorn.show()

    unicorn.setAll(0,255,200)
    time.sleep(0.3)
    unicorn.show()

    unicorn.setAll(0,255,0)
    time.sleep(0.3)
    unicorn.show()

    unicorn.setAll(0,0,255)
    time.sleep(0.3)
    unicorn.show()

    unicorn.setAll(155,0,155)
    time.sleep(0.3)
    unicorn.show()
