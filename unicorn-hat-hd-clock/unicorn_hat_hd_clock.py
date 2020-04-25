import unicornhathd as unicornhat
import time
import functools
from datetime import datetime as dt
import random

one = ["1111    "
,"1111    "
,"11      "
,"11      "
,"11      "
,"11      "
,"11      "
,"11      "]

two = ["22222222"
,"22222222"
,"22      "
,"22222222"
,"22222222"
,"      22"
,"22222222"
,"22222222"]

three = ["33333333"
,"33333333"
,"33      "
,"33333333"
,"33333333"
,"33      "
,"33333333"
,"33333333"]

four = ["44    44"
,"44    44"
,"44    44"
,"44444444"
,"44444444"
,"44      "
,"44      "
,"44      "]

five = ["55555555"
,"55555555"
,"      55"
,"55555555"
,"55555555"
,"55      "
,"55555555"
,"55555555"]

six = ["      66"
,"      66"
,"      66"
,"66666666"
,"66666666"
,"66    66"
,"66666666"
,"66666666"]

seven = ["77777777"
,"77777777"
,"77      "
,"77      "
,"77      "
,"77      "
,"77      "
,"77      "]

eight = ["88888888"
,"88888888"
,"88    88"
,"88888888"
,"88888888"
,"88    88"
,"88888888"
,"88888888"]

nine = ["99999999"
,"99999999"
,"99    99"
,"99999999"
,"99999999"
,"99      "
,"99      "
,"99      "]

zero = ["00000000"
,"00000000"
,"000   00"
,"00 0  00"
,"00  0 00"
,"00   000"
,"00000000"
,"00000000"]

n = [zero, one, two, three, four, five, six, seven, eight, nine]

def draw(pos, number, r=255, g=255, b=255, bg_color=(0,0,0)):
    x_shift = 0
    y_shift = 0
    if pos == 0:
        x_shift = 8
    elif pos == 2:
        x_shift = 8
        y_shift = 8
    elif pos == 3:
        y_shift = 8

    for y, num_line in enumerate(n[number]):
        for x, num_pixel in enumerate(num_line):
            if num_pixel == " ":
                unicornhat.set_pixel(x+x_shift, y+y_shift, bg_color[0], bg_color[1], bg_color[2])
            else:
                unicornhat.set_pixel(x+x_shift, y+y_shift, r, g, b)

try:
    cur_time = []
    col=1
    unicornhat.rotation(270)
    unicornhat.brightness(0.2)
    while True:
        now = dt.now()
        H0 = now.hour % 10
        H1 = int(now.hour / 10)
        M0 = now.minute % 10
        M1 = int(now.minute / 10)
        old_time = cur_time
        cur_time = [H1,H0, M1, M0]

        unicornhat.clear()

        if not old_time == cur_time:
            rand_colors = [[random.randint(0,255), random.randint(0,255), random.randint(0,255)],
            [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
            [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
            [random.randint(0,255), random.randint(0,255), random.randint(0,255)]]

        for x, digit in enumerate(cur_time):
            draw(x, digit, rand_colors[x][0],rand_colors[x][1],rand_colors[x][2])

        col+=1
        col%=2

        if col == 1:
            unicornhat.set_pixel(5, 7, 255*col,255*col,255*col)
            unicornhat.set_pixel(5, 8, 255*col,255*col,255*col)
            unicornhat.set_pixel(6, 7, 255*col,255*col,255*col)
            unicornhat.set_pixel(6, 8, 255*col,255*col,255*col)
            unicornhat.set_pixel(9, 7, 255*col,255*col,255*col)
            unicornhat.set_pixel(9, 8, 255*col,255*col,255*col)
            unicornhat.set_pixel(10, 7, 255*col,255*col,255*col)
            unicornhat.set_pixel(10, 8, 255*col,255*col,255*col)
        unicornhat.show()

        time.sleep(1.0)

except KeyboardInterrupt:
    unicornhat.off()