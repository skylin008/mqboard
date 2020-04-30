# This file is executed on every boot (including wake-boot from deepsleep)

import gc
gc.threshold(36500//4)

import sys
sys.path.append('/src')

from esp32 import Partition as p
print("Booting partition", p(p.RUNNING).info()[4])

import board
from board import connect_wifi
