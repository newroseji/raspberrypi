import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)


print 'Turning left...'
gpio.output(7, True)
gpio.output(15, False)

gpio.output(13, False)
gpio.output(11, False)

time.sleep(5)
print 'Done!'
gpio.cleanup()
