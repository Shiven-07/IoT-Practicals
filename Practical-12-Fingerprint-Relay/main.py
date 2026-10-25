from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as GPIO
from time import sleep

RELAY_PIN = 18  # BCM
ON, OFF = GPIO.HIGH, GPIO.LOW  # Source assumes active-HIGH relay.

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT, initial=OFF)
    try:
        sensor = PyFingerprint("/dev/serial0", 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise RuntimeError("Fingerprint sensor password is incorrect.")
        while True:
            print("Place finger.")
            while not sensor.readImage():
                sleep(0.05)
            sensor.convertImage(0x01)
            position, _ = sensor.searchTemplate()
            if position >= 0:
                print("Matched: bulb ON for five seconds.")
                GPIO.output(RELAY_PIN, ON)
                try:
                    sleep(5)
                finally:
                    GPIO.output(RELAY_PIN, OFF)
            else:
                GPIO.output(RELAY_PIN, OFF)
                print("Unmatched: bulb remains OFF.")
            sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.output(RELAY_PIN, OFF)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
