import logging
import pyfirmata
import time

ON = 1
OFF = 0
PIN = 8
# delay in seconds
DELAY = 10

board = pyfirmata.Arduino('/dev/ttyACM0')
board.digital[PIN].mode = pyfirmata.OUTPUT


def for_delay(delay_time):
    """
    Function to delay/wait for a certain time interval.
    :param delay_time: int, in secs
    :return: None
    """
    logging.warning(msg="In Delay function")
    time.sleep(delay_time)


def set_pin_high_low(pin, value):
    """
    Function to set pin to high.
    :param pin: int
    :param value: hex
    :return: None
    """
    logging.warning(msg="In set_pin_high_low function. value = {}".format(value))
    board.digital[pin].write(value)


def main():
    """Main function"""

    while True:
        set_pin_high_low(PIN, ON)
        for_delay(DELAY)
        set_pin_high_low(PIN, OFF)
        for_delay(DELAY)


if __name__ == "__main__":
    main()
