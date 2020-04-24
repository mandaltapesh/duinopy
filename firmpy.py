import logging
import pyfirmata
import time

ON = 1
OFF = 0
PIN = 8
# delay in seconds
DELAY = 1

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

    try:
        logging.warning(msg="In set_pin_high_low function. value = {}".format(value))
        board.digital[pin].write(value)
    except Exception as e:
        print(e)


def manual_main():
    """
    Function for manual toggling of LED
    :return: None
    """

    while True:
        choice = int(input("Enter a choice \n 1. Turn LED on [1] \n 2. Turn LED off \n 3. Quit [3] \n >> "))
        if choice == 1:
            set_pin_high_low(PIN, ON)
        elif choice == 2:
            set_pin_high_low(PIN, OFF)
        else:
            break


def auto_main():
    """
    Function to auto blink LED
    :return: None
    """
    counter = 9
    while counter:
        set_pin_high_low(PIN, ON)
        for_delay(DELAY)
        set_pin_high_low(PIN, OFF)
        for_delay(DELAY)
        counter -= 1


def main():
    """Main function"""

    while True:
        main_menu_choice = int(input(
            "Do you want to \n 1. Manually toggle the LED [1] \n 2. Auto blink on and off [2] \n 3. Quit \n >> "))

        if main_menu_choice == 1:
            manual_main()
        if main_menu_choice == 2:
            auto_main()
        else:
            board.exit()
            break


if __name__ == "__main__":
    main()
