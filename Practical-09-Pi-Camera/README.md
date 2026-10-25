# Practical 09: Capture an image and video

[Back to all practicals](../README.md)

**Source:** original PDF pages 39-41. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)

## Hardware and prerequisites

Raspberry Pi camera connected to CSI; Raspberry Pi OS with Picamera2. Install the OS python3-picamera2 package.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py in this folder. It creates captured_image.jpg and a ten-second captured_video.h264. Capture files are ignored by Git.

## Corrections and source gaps

Normalized the picam2 variable and replaced the invalid one-argument start_recording call with H264Encoder plus an output path. Added explicit still/video configuration and cleanup. Ignore copied RFID/fingerprint instructions in the source camera section.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
