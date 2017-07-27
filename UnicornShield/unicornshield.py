from neopixel import Adafruit_NeoPixel
import gpiozero
import time
import RPi.GPIO as gpio

# LEDs
leftEye = gpiozero.LED(21)
rightEye = gpiozero.LED(20)

# Button
button = gpiozero.Button(12)


# LED strip configuration:
LED_COUNT      = 9      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_CHANNEL    = 0       # PWM channel
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

ws2812 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
ws2812.begin()

# LEDs
def leftEyeOn():
    leftEye.on()

def leftEyeOff():
    leftEye.off()

def rightEyeOn():
    rightEye.on()

def rightEyeOff():
    rightEye.off()

# Button
def buttonPressed():
    return button.is_pressed

# Nose
def measure(pin):
    startTime = time.time()
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)
    time.sleep(0.1)
    gpio.setup(pin, gpio.IN)
    while gpio.input(pin) == 0:
        pass
    return time.time() - startTime

def nose():
    return measure(16)



def brightness(b=0.2):
    """Set the display brightness between 0.0 and 1.0

    0.2 is highly recommended, UnicornHat can get painfully bright!

    :param b: Brightness from 0.0 to 1.0 (default 0.2)
    """

    if b > 1 or b < 0:
        raise ValueError('Brightness must be between 0.0 and 1.0')

    """Absolute max brightness has been capped to 50%, do not change
    this unless you know what you're doing.
    UnicornHAT draws too much current above 50%."""
    brightness = int(b*128.0)
    if brightness < 30:
        print("Warning: Low brightness chosen, your UnicornHAT might not light up!")
    ws2812.setBrightness(brightness)


def getBrightness():
    """Get the display brightness value

    Returns a float between 0.0 and 1.0
    """
    return round(ws2812.getBrightness()/128.0, 3)


def clear():
    """Clear the buffer"""
    for x in range(LED_COUNT):
        setPixel(x, 0, 0, 0)
    show()


def off():
    """Clear the buffer and immediately update UnicornShield
    Turns off all pixels."""
    clear()
    show()


def setPixel(x, r, g, b):
    """Set a single pixel to RGB colour

    :param x: Number of LED from 0 to 9

    """
    # Because of wrong numbering
    positons = [0,1,2,3,7,5,6,8,4]
    ws2812.setPixelColorRGB(positons[x], r, g, b)


def getPixel(x ):
    """Get the RGB value of a single pixel
    """

    pixel = ws2812.getPixelColorRGB(x)
    return int(pixel.r), int(pixel.g), int(pixel.b)


def setAll(r, g, b):
    """Set all pixels to a specific colour"""
    for x in range(LED_COUNT):
        setPixel(x,r,g,b)

def show():
    """Update UnicornHat with the contents of the display buffer"""
    ws2812.show()
