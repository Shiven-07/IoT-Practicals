# Practical 13: MQTT publisher and LED subscriber

[Back to all practicals](../README.md)

**Source:** original PDF pages 56-60. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [subscriber.py](subscriber.py)
- [publisher.py](publisher.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Mosquitto broker on the Pi; LED through a resistor on BCM18/physical12, common GND.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Install/start Mosquitto on the Pi. In terminal 1 run python3 subscriber.py. In terminal 2 run python3 publisher.py. Enter ON or OFF; both use localhost and topic iot/led.

## Corrections and source gaps

Separated publisher/subscriber files. Updated callback signatures to Paho API VERSION2 and constrained requirements to Paho 2.x. Added the publisher network loop and delivery wait; subscriber cleans up GPIO.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
