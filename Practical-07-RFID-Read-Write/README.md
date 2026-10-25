# Practical 07: Read and write RFID tags

[Back to all practicals](../README.md)

**Source:** original PDF pages 24-28. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

MFRC522 RFID reader, compatible writable tag and SPI enabled. Physical pins: SDA/SS 24, SCK 23, MOSI 19, MISO 21, RST 22, 3.3V 1, GND 6.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py and choose write, read or clear. Record your own UID locally for later exercises. Only write to tags intended for your lab.

## Corrections and source gaps

Fixed RPI.GPIO capitalization and indentation. Clear now writes empty text rather than an undefined or previous text variable. Enable SPI; the source Serial instructions do not configure this SPI reader. Clearing text does not change the UID.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
