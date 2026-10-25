"""Require a configured RFID UID followed by any enrolled fingerprint."""
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from pyfingerprint.pyfingerprint import PyFingerprint
from RPLCD.i2c import CharLCD
from time import sleep, monotonic

AUTHORIZED_UID = None  # Replace with your own numeric UID from Practical 7.
BUZZER = 12  # BOARD pin 12 = BCM18; matches the RFID driver's BOARD mode.

def lcd_message(lcd, first, second=""):
    lcd.clear()
    lcd.write_string(first[:16])
    if second:
        lcd.crlf()
        lcd.write_string(second[:16])

def beep(count):
    for _ in range(count):
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.2)

def check_factors(uid, sensor, timeout=15):
    if uid != AUTHORIZED_UID:
        return False
    deadline = monotonic() + timeout
    while not sensor.readImage():
        if monotonic() >= deadline:
            return False
        sleep(0.05)
    sensor.convertImage(0x01)
    return sensor.searchTemplate()[0] >= 0

def main():
    if AUTHORIZED_UID is None:
        raise RuntimeError("Set AUTHORIZED_UID to your own card UID first.")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)
    lcd = None
    try:
        reader = SimpleMFRC522()
        lcd = CharLCD("PCF8574", 0x27, cols=16, rows=2)
        sensor = PyFingerprint("/dev/serial0", 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise RuntimeError("Fingerprint sensor password is incorrect.")
        while True:
            lcd_message(lcd, "Scan RFID Card")
            uid, _ = reader.read()
            if uid == AUTHORIZED_UID:
                lcd_message(lcd, "RFID Matched", "Place Finger")
            matched = check_factors(uid, sensor)
            lcd_message(lcd, "ACCESS", "GRANTED" if matched else "DENIED")
            print("ACCESS GRANTED" if matched else "ACCESS DENIED")
            beep(2 if matched else 4)
            sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.output(BUZZER, GPIO.LOW)
        GPIO.cleanup()
        if lcd is not None:
            lcd.close(clear=True)

if __name__ == "__main__":
    main()
