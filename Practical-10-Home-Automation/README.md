# Practical 10: Home automation using Flask

[Back to all practicals](../README.md)

**Source:** original PDF pages 42-45. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [app.py](app.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

Two compatible relay channels; BCM17/physical11 for light and BCM27/physical13 for fan. The code assumes active-HIGH relay inputs.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 app.py, then open http://<Pi-IP>:5000 on the same trusted lab network. Use a low-voltage demonstration load. For active-LOW boards reverse the ON and OFF constants before connecting loads.

## Corrections and source gaps

Fixed __name__, the main guard, quotes and indentation. Added return links and output cleanup. This deliberately simple lab server has no login or CSRF protection; do not expose it publicly.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
