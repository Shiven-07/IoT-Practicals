"""Lab prototype: a whitelisted RFID tag OR an enrolled fingerprint grants access."""
import csv
from datetime import datetime
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from pyfingerprint.pyfingerprint import PyFingerprint
from RPLCD.i2c import CharLCD

# BOARD numbering also keeps the MFRC522 reset on physical pin 22 (BCM25).
LED_PIN = 11    # BCM17
RELAY_PIN = 13  # BCM27, active-LOW
UNLOCK_TIME = 5
AUTHORIZED_UIDS = set()  # Add your own numeric UIDs; none are authorized initially.
LOG_FILE = "access_log.csv"

def lcd_message(lcd, first, second=""):
    lcd.clear()
    lcd.write_string(str(first)[:16])
    if second:
        lcd.crlf()
        lcd.write_string(str(second)[:16])

def create_log_file():
    try:
        with open(LOG_FILE, "x", newline="", encoding="utf-8") as stream:
            csv.writer(stream).writerow(["Timestamp", "Method", "Identifier", "Result"])
    except FileExistsError:
        pass

def log_event(method, identifier, result):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as stream:
        csv.writer(stream).writerow([
            datetime.now().isoformat(timespec="seconds"), method, identifier, result])

def unlock_door():
    GPIO.output(RELAY_PIN, GPIO.LOW)
    try:
        time.sleep(UNLOCK_TIME)
    finally:
        GPIO.output(RELAY_PIN, GPIO.HIGH)

def record_decision(lcd, method, identifier, granted):
    result = "GRANTED" if granted else "DENIED"
    print(f"[{result}] {method}: {identifier}")
    lcd_message(lcd, "ACCESS", result)
    log_event(method, identifier, result)
    if granted:
        GPIO.output(LED_PIN, GPIO.HIGH)
        try:
            unlock_door()
        finally:
            GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)

def check_rfid(reader, lcd):
    uid, _ = reader.read_no_block()
    if uid is None:
        return False
    record_decision(lcd, "RFID", uid, uid in AUTHORIZED_UIDS)
    return True

def check_fingerprint(sensor, lcd):
    if not sensor.readImage():
        return False
    sensor.convertImage(0x01)
    position, _ = sensor.searchTemplate()
    record_decision(lcd, "FINGERPRINT",
                    position if position >= 0 else "UNKNOWN", position >= 0)
    return True

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.HIGH)
    lcd = None
    try:
        lcd = CharLCD("PCF8574", 0x27, cols=16, rows=2)
        reader = SimpleMFRC522()
        sensor = PyFingerprint("/dev/serial0", 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise RuntimeError("Fingerprint sensor password is incorrect.")
        create_log_file()
        print("Ready. RFID whitelist size:", len(AUTHORIZED_UIDS))
        while True:
            lcd_message(lcd, "Scan Card or", "Place Finger")
            if check_rfid(reader, lcd):
                continue
            if check_fingerprint(sensor, lcd):
                continue
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Stopped")
    finally:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
        if lcd is not None:
            lcd.close(clear=True)

if __name__ == "__main__":
    main()
