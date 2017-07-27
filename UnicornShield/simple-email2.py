import unicornshield as unicorn
from time import sleep

while True:
    unicorn.setAll(0,0,0)
    unicorn.show()
    sleep(5)
    for x in range(130,230):
        unicorn.setAll(x,0,0)
        unicorn.show()
        sleep(0.05)
    sleep(4)
