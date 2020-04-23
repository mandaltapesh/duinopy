import pyfirmata
import time

ON = 1
OFF = 0
PIN = 8
# delay in seconds
DELAY = 4 

board = pyfirmata.Arduino('/dev/ttyACM0')


while True:
    board.digital[PIN].write(ON)
    time.sleep(DELAY)
    board.digital[PIN].write(OFF)
    time.sleep(DELAY)

