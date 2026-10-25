"""Read NMEA directly; do not let gpsd own the same serial port."""
import serial
import pynmea2

def main():
    with serial.Serial("/dev/serial0", baudrate=9600, timeout=1) as ser:
        try:
            while True:
                data = ser.readline().decode("ascii", errors="replace").strip()
                if not data.startswith(("$GPGGA,", "$GNGGA,")):
                    continue
                try:
                    msg = pynmea2.parse(data)
                except pynmea2.ParseError:
                    continue
                if int(msg.gps_qual or 0) == 0:
                    print("Waiting for a GPS fix...")
                    continue
                print("Latitude:", msg.latitude)
                print("Longitude:", msg.longitude)
                print("Altitude:", msg.altitude)
                print("--------------------------")
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
