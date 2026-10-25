# Practical 05: Plot ADS1115 gas-sensor readings

[Back to all practicals](../README.md)

**Source:** original PDF pages 17-20. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

ADS1115, MQ2 module, I2C enabled, graphical desktop for Matplotlib. Measure module voltages and use appropriate signal-level adaptation before connecting.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Run python3 main.py. Read A0 and plot a rolling 50-sample voltage history. Set the ADC address if your board is not at its library default.

## Corrections and source gaps

Fixed plt/pit and y_vals capitalization, split joined statements and restored indentation. Updated the ADS1x15 imports/channel API to the upstream example. Set a 0-4.096 V plot scale matching gain 1; the configured scale is not permission to exceed the ADC supply/input limits. This slow plot is not a general-purpose oscilloscope.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
