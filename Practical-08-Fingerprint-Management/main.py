"""Enrollment and template management; compatible serial sensor required."""
import os
import time
from pyfingerprint.pyfingerprint import PyFingerprint

PORT = os.environ.get("FINGERPRINT_PORT", "/dev/ttyUSB0")

def wait_for_finger(sensor):
    while not sensor.readImage():
        time.sleep(0.05)

def enroll(sensor):
    print("Place finger.")
    wait_for_finger(sensor)
    sensor.convertImage(0x01)
    position, _ = sensor.searchTemplate()
    if position >= 0:
        print("Already enrolled at position", position)
        return
    print("Remove finger.")
    while sensor.readImage():
        time.sleep(0.05)
    time.sleep(1)
    print("Place the same finger again.")
    wait_for_finger(sensor)
    sensor.convertImage(0x02)
    if sensor.compareCharacteristics() == 0:
        raise ValueError("The two scans do not match.")
    sensor.createTemplate()
    print("Stored at position", sensor.storeTemplate())

def search(sensor):
    print("Place finger.")
    wait_for_finger(sensor)
    sensor.convertImage(0x01)
    position, score = sensor.searchTemplate()
    print("No match" if position < 0 else f"Matched position {position}; score {score}")

def main():
    sensor = PyFingerprint(PORT, 57600, 0xFFFFFFFF, 0x00000000)
    if not sensor.verifyPassword():
        raise RuntimeError("Fingerprint sensor password is incorrect.")
    try:
        while True:
            print("\n1. Enroll\n2. Search\n3. Delete\n4. Count\n5. Exit")
            option = input("Option: ").strip()
            try:
                if option == "1":
                    enroll(sensor)
                elif option == "2":
                    search(sensor)
                elif option == "3":
                    position = int(input("Template position to delete: "))
                    if not 0 <= position < sensor.getStorageCapacity():
                        raise ValueError("Position is outside this sensor's capacity.")
                    print("Deleted" if sensor.deleteTemplate(position) else "Not deleted")
                elif option == "4":
                    print(f"{sensor.getTemplateCount()}/{sensor.getStorageCapacity()}")
                elif option == "5":
                    break
            except Exception as exc:
                print("Operation failed:", exc)
    except KeyboardInterrupt:
        print("\nStopped")

if __name__ == "__main__":
    main()
