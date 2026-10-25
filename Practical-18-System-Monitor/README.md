# Practical 18: Monitor CPU, memory and temperature

[Back to all practicals](../README.md)

**Source:** original PDF pages 78-82. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Raspberry Pi OS and psutil. Python 3.9 or newer for the string helpers used here.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py. CPU and memory are sampled repeatedly; vcgencmd supplies temperature. If unavailable, temperature displays unavailable rather than crashing.

## Corrections and source gaps

Repaired indentation, quotes and f-strings; replaced shell-based temperature reading with a bounded subprocess call and numeric parsing.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
