# Practical 08: Enroll, search and delete fingerprints

[Back to all practicals](../README.md)

**Source:** original PDF pages 29-38. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Supported UART fingerprint sensor, connected through a compatible USB-to-UART adapter for /dev/ttyUSB0 or directly through UART.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py. Set FINGERPRINT_PORT=/dev/serial0 for a direct UART sensor. Enroll before trying the later fingerprint practicals. Sensors store templates internally; this repository contains no captured fingerprint data.

## Corrections and source gaps

Reconstructed malformed functions, strings and method names (convertImage/createTemplate), corrected /dev/ttyUSB0 and hex values, restored the entry point, and added duplicate-enrollment return plus sensor-capacity validation. A generic USB fingerprint scanner is not automatically compatible with pyfingerprint.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
