from picamera2 import Picamera2
import cv2
import time
from RPLCD.i2c import CharLCD

def main():
    lcd = CharLCD("PCF8574", 0x27, cols=16, rows=2)
    camera = Picamera2()
    try:
        config = camera.create_preview_configuration(
            main={"size": (640, 480), "format": "RGB888"})
        camera.configure(config)
        camera.start()
        time.sleep(2)
        previous = cv2.cvtColor(camera.capture_array(), cv2.COLOR_BGR2GRAY)
        while True:
            current = cv2.cvtColor(camera.capture_array(), cv2.COLOR_BGR2GRAY)
            difference = cv2.absdiff(previous, current)
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
            message = "Motion Detected" if cv2.countNonZero(threshold) > 5000 else "No Motion"
            lcd.clear()
            lcd.write_string(message)
            print(message)
            previous = current
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        camera.close()
        lcd.close(clear=True)

if __name__ == "__main__":
    main()
