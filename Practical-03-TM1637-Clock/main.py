"""Requires the lab's tm1637.py driver with the capitalized API below."""
import datetime
import time
import tm1637

def main():
    display = tm1637.TM1637(CLK=21, DIO=20, brightness=5.0)
    display.Clear()
    try:
        while True:
            now = datetime.datetime.now()
            digits = [now.hour // 10, now.hour % 10,
                      now.minute // 10, now.minute % 10]
            display.Show(digits)
            display.ShowDoublepoint(now.second % 2)
            time.sleep(0.25)
    except KeyboardInterrupt:
        pass
    finally:
        display.Clear()

if __name__ == "__main__":
    main()
