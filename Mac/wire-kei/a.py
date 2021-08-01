# -*- coding: utf-8 -*-
import wiringpi as pi
import time

INPUT_PIM = 17

pi.wiringPiSetupGpio()
pi.pinMode(INPUT_PIM, pi.OUTPUT)
i = 0

while True:
    try:
        pi.digitalWrite(INPUT_PIM, pi.HIGH)
        time.sleep(0.4)
        pi.digitalWrite(INPUT_PIM, pi.LOW)
        time.sleep(0.4)
        i += 1
        print("{}回目です。".format(i))
    except KeyboardInterrupt:
        pass

