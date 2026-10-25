# Practical 11: Show fingerprint match status on an LCD

[Back to all practicals](../README.md)

**Source:** original PDF pages 46-50. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Enrolled fingerprint sensor on UART and an I2C 16x2 LCD at 0x27. Enable UART and I2C.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Enroll using Practical 8 with FINGERPRINT_PORT=/dev/serial0, then run python3 main.py. LCD shows Matched or Unmatched.

## Corrections and source gaps

Normalized formatting, added a short polling delay and LCD cleanup. Use RPLCD with its i2c module; the source RPLCD-i2c package name is not required.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
