# Practical 16: Camera motion detection with LCD feedback

[Back to all practicals](../README.md)

**Source:** original PDF pages 71-76. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

CSI camera, Picamera2, OpenCV, and a 16x2 I2C LCD. Install OS python3-picamera2 and python3-opencv packages.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Enable I2C, set the LCD address, and run python3 main.py. Motion is reported when more than 5000 pixels change above threshold 25 between frames.

## Corrections and source gaps

Repaired Picamera2/cv2 imports, dictionary syntax, names, indentation and LCD configuration. Chose RGB888 output with the documented OpenCV BGR interpretation; added camera/LCD cleanup. Lighting changes can trigger this simple detector.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
