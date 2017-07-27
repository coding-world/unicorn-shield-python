import unicornshield as unicorn
from time import sleep

while True:
    if unicorn.nose() > 0.3:
        for x in range(9):
            unicorn.setPixel(x,155,0,155)
            unicorn.show()
            time.sleep(0.15)
        for x in range(9):
            unicorn.setPixel(x,0,0,0)
            unicorn.show()
            time.sleep(0.05)
