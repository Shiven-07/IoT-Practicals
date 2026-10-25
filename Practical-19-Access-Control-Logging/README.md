# Practical 19: RFID or fingerprint access control with logging

[Back to all practicals](../README.md)

**Source:** original PDF pages 82-98. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

MFRC522, enrolled UART fingerprint sensor, I2C LCD, LED and active-LOW relay. Physical pins: LED 11 (BCM17), relay 13 (BCM27), RFID reset 22 (BCM25).

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Enable SPI/UART/I2C. Populate AUTHORIZED_UIDS with your own tag numbers and enroll fingers using Practical 8. Run python3 main.py. Either a whitelisted RFID tag OR an enrolled fingerprint grants access. access_log.csv stays local and is ignored by Git.

## Corrections and source gaps

Reconstructed the damaged code, restored the absent main polling loop, corrected serial0/identifiers/strings, and made GPIO numbering consistently BOARD for the RFID driver. Added initial locked state and finally blocks that restore the relay after an interrupted pulse. Empty whitelist rejects all RFID tags until configured. This exercise is OR authentication, unlike Practical 15. It is a lab prototype, not a deployed door-security system.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
