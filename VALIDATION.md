# Validation

Prepared on 25 October 2026.

- All 20 split PDFs reopened successfully: 108 page instances cover every one of the 100 original pages, including eight shared boundary pages.
- Each split page has the same content stream, dimensions, extracted text and embedded image data as its source page.
- The full original PDF is byte-for-byte unchanged.
- All 100 source pages were rendered and visually reviewed in contact sheets. The first and last page of every split PDF was also rendered: all 40 were pixel-identical to the corresponding original render.
- All 19 Python source files passed Python syntax parsing.
- Four groups of behavior checks passed using mocked GPIO, sensor and MQTT objects: MQTT ON/OFF/invalid commands; both-factor authentication; matched/unmatched relay branches and cleanup; RFID/fingerprint access decisions, CSV logging and interrupted relay-pulse cleanup.
- Catalog entries and local Markdown links were checked.

## What is not verified

No physical Raspberry Pi, sensor, relay, LCD or camera was connected to this environment. Hardware imports, package installation, electrical connections, physical outputs and real service behavior were not tested. The behavior checks use test doubles and do not prove device compatibility.

Flask is not installed in the validation environment, so the Flask apps received syntax checks only. No live Telegram or MQTT broker connection was attempted. The UWP code was not compiled or deployed. The TM1637 driver is not supplied, and the Node-RED practical has no flow export to validate.

Original PDF screenshots are reference images, not outputs from these checks. See SOURCE-NOTES.md and each practical README for corrections and missing items.
