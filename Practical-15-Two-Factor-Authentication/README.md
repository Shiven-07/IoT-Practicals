# Practical 15: RFID and fingerprint two-factor demonstration

[Back to all practicals](../README.md)

**Source:** original PDF pages 64-71. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

MFRC522 + enrolled UART fingerprint sensor + I2C LCD + small compatible buzzer at physical pin12 (BCM18).

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Enable SPI, UART and I2C. Set AUTHORIZED_UID to your own card UID. Run python3 main.py. The card must match before the program checks an enrolled finger, with a 15-second wait limit.

## Corrections and source gaps

Repaired identifiers, indentation and the missing waiting-loop body. Uses BOARD numbering to agree with the RFID driver and avoid its BCM reset-pin ambiguity. No example UID is authorized by default. Added cleanup and a timeout. As in the source, any enrolled fingerprint can follow the configured card; it does not bind a particular finger to a particular card.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
