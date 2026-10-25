from pyfingerprint.pyfingerprint import PyFingerprint
from RPLCD.i2c import CharLCD
from time import sleep

def main():
    lcd = CharLCD("PCF8574", 0x27, cols=16, rows=2)
    try:
        sensor = PyFingerprint("/dev/serial0", 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise RuntimeError("Fingerprint sensor password is incorrect.")
        while True:
            lcd.clear()
            lcd.write_string("Place Finger")
            while not sensor.readImage():
                sleep(0.05)
            sensor.convertImage(0x01)
            position, _ = sensor.searchTemplate()
            status = "Matched" if position >= 0 else "Unmatched"
            lcd.clear()
            lcd.write_string("Fingerprint")
            lcd.crlf()
            lcd.write_string(status)
            print("Fingerprint", status)
            sleep(3)
    except KeyboardInterrupt:
        pass
    finally:
        lcd.close(clear=True)

if __name__ == "__main__":
    main()
