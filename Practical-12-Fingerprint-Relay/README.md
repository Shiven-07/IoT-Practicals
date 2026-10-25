# Practical 12: Simulate a fingerprint door lock with a relay

[Back to all practicals](../README.md)

**Source:** original PDF pages 51-56. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Enrolled UART fingerprint sensor and an active-HIGH relay on BCM18/physical12.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py using a low-voltage lamp demonstration. A matched fingerprint energizes the relay for five seconds; an unmatched print leaves it off.

## Corrections and source gaps

Moved the match decision inside the polling loop, restored indentation, added initial output state and shutdown cleanup. Polarity differs from Practical 19: configure it for the actual relay.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
