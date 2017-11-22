import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

    print 'Initialization done!'


def forward(tf):
    print 'Moving Forward...'
    gpio.output(7, True)
    gpio.output(13, True)
    gpio.output(11, False)  # New Line
    gpio.output(15, False)  # New Line

    time.sleep(tf)
    gpio.cleanup()


def reverse(tf):
    print 'Moving Backward...'
    gpio.output(11, True)
    gpio.output(15, True)
    gpio.output(7, False)  # New Line
    gpio.output(13, False)  # New Line

    time.sleep(tf)
    gpio.cleanup()


def turn_left(tf):
    print 'Turning Left...'
    gpio.output(7, True)
    gpio.output(15, False)  # New Line
    gpio.output(13, False)  # New Line
    gpio.output(11, False)  # New Line
    time.sleep(tf)
    gpio.cleanup()


def turn_right(tf):
    print 'Turning Right...'
    gpio.output(11, True)
    gpio.output(13, False)  # New Line
    gpio.output(7, False)  # New Line
    gpio.output(15, False)  # New Line

    time.sleep(tf)
    gpio.cleanup()


def pivot_left(tf):
    print 'Pivoting Left...'
    gpio.output(7, True)
    gpio.output(15, True)
    gpio.output(13, False)  # New Line
    gpio.output(11, False)  # New Line
    time.sleep(tf)
    gpio.cleanup()


def pivot_right(tf):
    print 'Pivoting Right...'
    gpio.output(13, True)
    gpio.output(11, True)
    gpio.output(7, False)  # New Line
    gpio.output(15, False)  # New Line
    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    init()

    print 'Key: ', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
    else:
        pass


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
