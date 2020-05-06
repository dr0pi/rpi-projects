#!/usr/bin/env python3

import asyncio
import time
from datetime import datetime as dt
import random
from unicornhatmini import UnicornHATMini

nums = [None] * 10
nums[0] = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
nums[1] = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
nums[2] = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
nums[3] = [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
nums[4] = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]
nums[5] = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
nums[6] = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
nums[7] = [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
nums[8] = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
nums[9] = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.2)
unicornhatmini.set_rotation(180)


async def main():
    old_M0 = -1
    while True:
        now = dt.now()
        H0 = now.hour % 10
        H1 = int(now.hour / 10)
        M0 = now.minute % 10
        M1 = int(now.minute / 10)
        cur_time = [H1, H0, M1, M0]
        show_colon = (now.second % 2) == 0

        if old_M0 != M0:
            old_M0 = M0
            rand_colors = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
                           [random.randint(0, 255), random.randint(
                               0, 255), random.randint(0, 255)],
                           [random.randint(0, 255), random.randint(
                               0, 255), random.randint(0, 255)],
                           [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]]

        unicornhatmini.clear()

        for digit in range(0, 4):
            draw(digit, nums[cur_time[digit]], rand_colors[digit])

        if show_colon:
            unicornhatmini.set_pixel(8, 2, 255, 255, 255)
            unicornhatmini.set_pixel(8, 4, 255, 255, 255)

        unicornhatmini.show()

        await asyncio.sleep(1)


def draw(position, num, color):
    for i in range(0, 20):
        x = i % 4
        y = int(i / 4)+1

        eff_x = x+(4*position)
        if position > 1:
            eff_x = eff_x+1
        eff_r = color[0]*num[i]
        eff_g = color[1]*num[i]
        eff_b = color[2]*num[i]

        unicornhatmini.set_pixel(eff_x, y, eff_r, eff_g, eff_b)


asyncio.run(main())
