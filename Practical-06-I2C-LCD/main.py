from RPLCD.i2c import CharLCD
from time import sleep

def main():
    lcd = CharLCD("PCF8574", 0x27, port=1, cols=16, rows=2)
    try:
        lcd.clear()
        lcd.write_string("Hello Students!")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Raspberry Pi 4")
        sleep(10)
    finally:
        lcd.close(clear=True)

if __name__ == "__main__":
    main()
