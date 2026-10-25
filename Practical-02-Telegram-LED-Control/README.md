# Practical 02: Control an LED using Telegram

[Back to all practicals](../README.md)

**Source:** original PDF pages 4-10. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [main.py](main.py)
- [.env.example](.env.example)
- [requirements.txt](requirements.txt)

## Hardware and prerequisites

One LED and series resistor on physical pin 11 (BCM17); internet connection and your own Telegram bot.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID as environment variables, then run python3 main.py. Send on, off or stop from that chat. The .env.example file is a template only: the program does not automatically load it.

## Corrections and source gaps

Converted Python 2 print statements to Python 3; restored indentation; removed the undefined TelegramError block; stop now signals the main thread; added cleanup and a chat-ID allowlist. Uses the PDF legacy telepot library, whose live service compatibility has not been tested.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.
