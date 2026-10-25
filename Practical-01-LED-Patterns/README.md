# Practical 01: LED blinking patterns

[Back to all practicals](../README.md)

**Source:** original PDF pages 1-3. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Two LEDs, series resistors, Raspberry Pi 4; physical pins 29 and 31, with common GND.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py. The sequence is 10, 01, 11, 00 with a half-second delay.

## Corrections and source gaps

Restored the finally-block indentation; combined repeated output calls without changing the sequence.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
