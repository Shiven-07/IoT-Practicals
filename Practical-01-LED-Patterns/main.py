"""Two-bit LED sequence; BOARD means physical header pin numbers."""
import RPi.GPIO as GPIO
from time import sleep

LED1, LED2 = 29, 31

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup((LED1, LED2), GPIO.OUT, initial=GPIO.LOW)
    try:
        while True:
            for pattern in ((1, 0), (0, 1), (1, 1), (0, 0)):
                GPIO.output((LED1, LED2), pattern)
                sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.output((LED1, LED2), (0, 0))
        GPIO.cleanup()

if __name__ == "__main__":
    main()
