# Practical 06: Display text on a 16x2 I2C LCD

[Back to all practicals](../README.md)

**Source:** original PDF pages 21-23. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

16x2 LCD with PCF8574 backpack, I2C enabled; SDA BCM2 (pin 3), SCL BCM3 (pin 5).

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Use i2cdetect -y 1 to identify the address. Set 0x27 or the actual address in main.py, then run python3 main.py.

## Corrections and source gaps

Fixed Icd/lcd inconsistencies and the broken lcd.clear call; added clear/close cleanup.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
