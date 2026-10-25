# Practical 04: Read coordinates from a GPS module

[Back to all practicals](../README.md)

**Source:** original PDF pages 13-16. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

GPS serial module: TX to BCM15/RXD (physical 10), RX to BCM14/TXD (physical 8), common GND.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Enable UART and disable the serial login shell. Run python3 main.py. This script reads /dev/serial0 directly at 9600 baud; stop any gpsd process that owns that port first. Outdoor sky visibility may be needed for a fix.

## Corrections and source gaps

Restored indentation; added GNGGA support, malformed-sentence handling and no-fix handling. Source command spacing errors include ls /dev/serial*, cgps -s and gpsd /dev/serial0 -F /var/run/gpsd.sock. The daemon approach is an alternative, not a prerequisite for this direct-serial script.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
