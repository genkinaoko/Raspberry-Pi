# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

OUTPUT = 17 # 抵抗に繋いだ側の、GPIOポート番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT, GPIO.OUT)
i = 0
while True:
    try:
        GPIO.output(OUTPUT, True) # 点灯 Trueの代わりにGPIO.HIGHでもOK
        time.sleep(0.1)
        GPIO.output(OUTPUT, False) # 消灯 Falseの代わりにGPIO.LOWでもOK
        time.sleep(0.1)
        print("{}回目".format(i))
        i += 1
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("終了です!")
    