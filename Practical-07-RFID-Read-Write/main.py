import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

def main():
    GPIO.setmode(GPIO.BOARD)
    reader = SimpleMFRC522()
    try:
        while True:
            print("\n1. Write tag\n2. Read tag\n3. Clear tag text\nOther. Exit")
            option = input("Option: ").strip()
            if option == "1":
                text = input("New text (up to 48 ASCII characters): ")
                text.encode("ascii")
                print("Place your tag.")
                reader.write(text[:48])
                print("Written")
            elif option == "2":
                print("Place your tag.")
                uid, text = reader.read()
                print("UID:", uid)
                print("Text:", text)
            elif option == "3":
                print("Place the tag whose stored text you want to clear.")
                reader.write("")
                print("Text cleared; the UID is unchanged.")
            else:
                break
            sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
