# Practical 03: Display the current time on TM1637

[Back to all practicals](../README.md)

**Source:** original PDF pages 11-12. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)

## Hardware and prerequisites

TM1637 display: CLK BCM21 (physical 40), DIO BCM20 (physical 38), common GND. Confirm module logic-level compatibility.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Obtain the lab-provided tm1637.py and place it beside main.py; then run python3 main.py. It must support TM1637, Clear, Show and ShowDoublepoint with the shown constructor.

## Corrections and source gaps

Restored indentation and removed repeated clearing. The PDF does not supply the driver. Packages sharing the tm1637 name can have different APIs; do not substitute blindly.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
