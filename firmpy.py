import pyfirmata
import time

ON = 0x1
OFF = 0x0
PIN = 8
# delay in seconds
DELAY = 8

board = pyfirmata.Arduino('/dev/ttyACM0')


def main():
    """Main function"""

    while True:
        board.digital[PIN].write(ON)
        time.sleep(DELAY)
        board.digital[PIN].write(OFF)
        time.sleep(DELAY)


if __name__ == "__main__":
    main()
