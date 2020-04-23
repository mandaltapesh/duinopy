import logging
import pyfirmata
import time

ON = 1
OFF = 0
PIN = 8
# delay in seconds
DELAY = 10

board = pyfirmata.Arduino('/dev/ttyACM2')
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
    # import pdb;
    # pdb.set_trace()

    logging.warning(msg="In set_pin_high_low function. value = {}".format(value))
    board.digital[pin].write(value)

    
def main():
    """Main function"""

    while True:
        choice = int(input("Enter a choice \n 1. Turn LED on [1] \n 2. Turn LED off \n 3. Quit [3] \n >> "))
        if choice == 1:
            set_pin_high_low(PIN, ON)
            for_delay(DELAY)
        elif choice == 2:
            set_pin_high_low(PIN, OFF)
            for_delay(DELAY)
        else:
            board.exit()
            break


if __name__ == "__main__":
    main()
