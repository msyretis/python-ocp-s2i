#! /bin/python3
import time

while True:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(current_time)
    time.sleep(1)